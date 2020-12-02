from django.shortcuts import render
from django.http import HttpResponse
from .models import listModel
import random

# Create your views here.

def index(request):

    return HttpResponse('Hey there!!!')

def home(request):

    return render(request, 'password/home.html', {'password' : '1234ABCD'})

def generatepassword(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('Length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))
    
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    thepassword = ''

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'password/generate.html',{'thepassword' : thepassword})

def about(request):
    return render(request, 'password/about.html')