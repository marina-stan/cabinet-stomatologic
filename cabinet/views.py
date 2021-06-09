from django.http import HttpResponse
from django.shortcuts import render
import operator
from managementcabinet.models import Medic

def home(request):
    return render(request, 'home.html')

def about(request):
    medici = Medic.objects
    return render(request, 'about.html',  {'medici':medici})

def contact(request):
    return render(request, 'contact.html')

def consultatii(request):
    return render(request, 'consultatii-online.html')

def conectare(request):
    return render(request, 'conectare.html')

def contulMeu(request):
    return render(request, 'contul-meu.html')

def medici(request):
    return render(request, 'medici.html')
