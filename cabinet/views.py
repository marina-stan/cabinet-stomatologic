from django.http import HttpResponse
from django.shortcuts import render
import operator
from managementcabinet.models import Person
from managementcabinet.models import Medic
from managementcabinet.models import Asistent
from managementcabinet.models import Pacient
from django.contrib.auth.models import User, Group
from django.contrib import auth
from django.contrib.auth import authenticate, login
from cabinet.forms import contactformemail
from django.core.mail import EmailMessage, send_mail

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

def asistenti(request):
    return render(request, 'asistenti.html')

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
