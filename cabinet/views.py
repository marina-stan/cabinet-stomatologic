from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, FormView
import operator
import datetime
from datetime import datetime
from managementcabinet.models import *
from django.contrib.auth.models import User, Group
from django.contrib import auth
from django.contrib.auth import authenticate, login
from cabinet.forms import contactformemail
from cabinet.forms import DateForm
from django.core.mail import EmailMessage, send_mail

def home(request):
    return render(request, 'home.html')

def about(request):
    medici = Medic.objects
    return render(request, 'about.html', {'medici':medici})

def contact(request):
    return render(request, 'contact.html')

def consultatii(request):
    return render(request, 'consultatii-online.html')

def contulMeu(request):
    pacienti = Pacient.objects
    programari = Programare.objects
    form = DateForm()
    
    context = {'pacienti':pacienti, 'programari':programari, 'form':form}
    # if form.is_valid():
    #     prog_date=form.cleaned_data['date_input']
    #     return HttpResponseRedirect(reverse('contul-meu.html'))
    return render(request, 'contul-meu.html', context)

def medici(request):
    medici = Medic.objects
    pacienti = Pacient.objects
    asistenti = Asistent.objects
    programari = Programare.objects
    fise_pacienti = FisaPacient.objects
    facturi = Factura.objects
    diagnostice = Diagnostic.objects
    tratamente = Tratament.objects
    produse = Produs.objects
    context = {'medici':medici, 'pacienti':pacienti, 'asistenti':asistenti, 'programari':programari, 'fise_pacienti':fise_pacienti,
               'facturi':facturi, 'diagnostice':diagnostice, 'tratamente':tratamente, 'produse':produse}
    return render(request, 'medici.html', context)

def asistenti(request):
    asistenti = Asistent.objects
    pacienti = Pacient.objects
    programari = Programare.objects
    fise_pacienti = FisaPacient.objects
    facturi = Factura.objects
    context = {'pacienti':pacienti, 'asistenti':asistenti, 'programari':programari, 'fise_pacienti':fise_pacienti, 'facturi':facturi}
    return render(request, 'asistenti.html', context)

def is_medic(user):
    return user.groups.filter(name='Medici').exists()

def is_asistent(user):
    return user.groups.filter(name='Asistenti').exists()

def is_pacient(user):
    return user.groups.filter(name='Pacienti').exists()

def conectare(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            if is_medic(user):
                return render(request, 'medici.html')
            elif is_asistent(user):
                return render(request, 'asistenti.html')
            elif is_pacient(user):
                return render(request, 'contul-meu.html')
        else:
            return render(request, 'conectare.html', {'error':'*Adresa de email sau parola sunt gresite!' })
    else:
        return render(request, 'conectare.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return render(request, 'conectare.html')
    return render(request, 'conectare.html')



def contactsendemail(request):
    if request.method == "GET":
        form = contactformemail()
    else:
        form = contactformemail(request.POST, request.FILES)
        if form.is_valid():
            fromemail = form.cleaned_data['fromemail']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            email = EmailMessage(subject, body, [fromemail], ['softdentsmart@gmail.com'])
            try:
                uploaded_file = request.FILES['uploaded_file']
                email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)
                print(uploaded_file)
                email.send()
                return HttpResponse('Mesajul CU atasament a fost trimis cu succces !')
            except:
                email.send()
                return HttpResponse('Mesajul FARA atasament a fost trimis cu succces !')

    return render(request, 'consultatii-online.html', {'form':form})
