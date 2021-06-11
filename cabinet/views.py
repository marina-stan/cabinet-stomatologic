from django.http import HttpResponse
from django.shortcuts import render
import operator
from managementcabinet.models import Medic
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'home.html')

def about(request):
    medici = Medic.objects
    return render(request, 'about.html',  {'medici':medici})

def contact(request):
    return render(request, 'contact.html')

def consultatii(request):
    return render(request, 'consultatii-online.html')

def contulMeu(request):
    return render(request, 'contul-meu.html')

def medici(request):
    return render(request, 'medici.html')

def conectare(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return render(request, 'contul-meu.html')
        else:
            return render(request, 'conectare.html', {'error':'Adresa de email sau parola sunt gresite!' })
    else:
        return render(request, 'conectare.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return render(request, 'conectare.html')
    return render(request, 'conectare.html')
