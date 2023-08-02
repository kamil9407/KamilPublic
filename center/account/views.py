from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect

from .models import UserProfile

from .forms import CreateUserForm, LoginForm, UpdateUserForm, UserProfileForm

from django.contrib.sites.shortcuts import get_current_site

from .token import user_tokenizer_generator

from django.template.loader import render_to_string

from django.utils.encoding import force_bytes, force_str

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.contrib.auth.models import User

from django.contrib.auth.models import auth

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.core.files.storage import FileSystemStorage


from django.shortcuts import render
from .models import UserProfile


def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            user = form.save()

            user.is_active = False

            user.save()

            current_site = get_current_site(request)

            subject = "Email weryfikacyjny konta."

            message = render_to_string('account/email-verification.html',{
                'user':user,
                'domain':current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': user_tokenizer_generator.make_token(user),
            })

            user.email_user(subject=subject, message = message)

            return redirect('weryfikacja-emaila-wyslana')

    context = {'form':form}

    return render (request, 'account/registration/register.html', context = context)

def user_profile_list(request):
    user_profiles = UserProfile.objects.all()
    return render(request, 'user_profile_list.html', {'user_profiles': user_profiles})

@login_required(login_url='logowanie')
def dashboard(request):
    my_user = UserProfile.objects.get(id=26)
    context = {'my_user': my_user}
    return render(request, 'account/dashboard.html', context=context)


@login_required(login_url='logowanie')
def user_profile(request):

    if request.method == 'POST':

        profile_form = UserProfileForm(request.POST, request.FILES)

        if profile_form.is_valid:

            profile_form.save()

        return redirect('panel-uzytkownika')
    else:
        profile_form = UserProfileForm()



    return render(request, 'account/user-profile.html', {'profile_form':profile_form})

    
            

    
def email_verification(request, uidb64, token):

    unique_id = force_str(urlsafe_base64_decode(uidb64))

    user = User.objects.get(pk=unique_id)

    if user and user_tokenizer_generator.check_token(user, token):

        user.is_active = True

        user.save()

        return redirect('weryfikacja-emaila-udana')
    
    else:

        return redirect('weryfikacja-emaila-nieudana')

    return render(request, 'account/email-verification.html')

def email_verification_sent(request):

    return render(request, 'account/email-verification-sent.html')

def email_verification_success(request):

    return render(request, 'account/email-verification-success.html')

def email_verification_fail(request):

    return render(request, 'account/email-verification-fail.html')

def login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data = request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("panel-uzytkownika")
    
    context = {'form':form}

    return render(request, 'account/login.html', context=context)


def logout(request):

    auth.logout(request)

    return redirect('start')

@login_required(login_url = 'logowanie')
def profile_management(request):    

    # Updating our user's username and email

    

    user_form = UpdateUserForm(instance=request.user)

    if request.method == 'POST':

        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():

            user_form.save()

            return redirect("panel-uzytkownika")

   

    context = {'user_form':user_form}

    return render(request, 'account/profile-management.html', context=context)

@login_required(login_url = 'logowanie')
def delete_account(request):

    user = User.objects.get(id = request.user.id)

    if request.method == 'POST':

        user.delete()

        return redirect('start')

    return render(request, 'account/delete-account.html')

