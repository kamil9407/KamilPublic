from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User

from django import forms

from .models import UserProfile

from django.forms import ModelForm

from django.forms.widgets import PasswordInput, TextInput





class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ['name', 'lastname', 'city', 'zipcode', 'division', 'profile_picture']
        

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User

        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):

        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True

    def clean_email(self):

        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():

            raise forms.ValidationError('Ten email jest nieprawidłowy')
        
        if len(email) >= 350:

            raise forms.ValidationError('Twój email jest za długi')
    
        return email 

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())

    password = forms.CharField(widget=PasswordInput())

#Update form

class UpdateUserForm(forms.ModelForm):

    password = None

    class Meta:

        model = User

        fields = ['username', 'email']
        exclude = ['password1', 'password1']

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
    
        self.fields['email'].required = True
    
    def clean_email(self):

        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():

            raise forms.ValidationError('Ten email jest niewłaściwy')

        # len function updated ###

        if len(email) >= 350:

            raise forms.ValidationError("Ten email jest zbyt długi")


        return email


