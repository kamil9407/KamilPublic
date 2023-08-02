from django.shortcuts import render
from .models import Kategoria
# Create your views here.

def start(request):

    all_categories = Kategoria.objects.all()

    context = {'site_category': all_categories}

    return render (request, 'opinions/start.html', context = context)