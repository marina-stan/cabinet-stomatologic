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
from cabinet.forms import FormModelPacient
from cabinet.forms import FormModelProgramare
from cabinet.forms import FormModelFisa
from cabinet.forms import FormModelProdus
from cabinet.forms import FormModelFactura
from cabinet.forms import FormModelDiagnostic
from cabinet.forms import FormModelTratament
from cabinet.forms import FormModelProgramarePacient
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


def adaugapacient(request):
    form = FormModelPacient(request.POST)
    if form.is_valid():
        form.save()
        nume_de_familie = form.cleaned_data['nume_de_familie']
        prenume = form.cleaned_data['prenume']
        cnp = form.cleaned_data['cnp']
        email = form.cleaned_data['email']
        numar_de_telefon = form.cleaned_data['numar_de_telefon']
        adresa = form.cleaned_data['adresa']
        note = form.cleaned_data['note']
        persoana_de_contact = form.cleaned_data['persoana_de_contact']
        status = form.cleaned_data['status']
        form = FormModelPacient()
        return HttpResponse('Pacientul a fost adaugat cu succces !')
    return render(request, 'adaugapacient.html')

def adaugaprogramare(request):
    pacienti = Pacient.objects
    medici = Medic.objects
    asistenti = Asistent.objects
    form = FormModelProgramare(request.POST)
    if form.is_valid():
        form.save()
        pacient = form.cleaned_data['pacient']
        medic = form.cleaned_data['medic']
        asistent = form.cleaned_data['asistent']
        data_si_ora = form.cleaned_data['data_si_ora']
        durata_in_minute = form.cleaned_data['durata_in_minute']
        notes = form.cleaned_data['notes']
        status = form.cleaned_data['status']
        form = FormModelProgramare()
        return HttpResponse('Programarea a fost adaugată cu succces !')
    form = FormModelProgramare()
    context = {'pacienti':pacienti,'medici':medici,'asistenti':asistenti, 'form':form}
    return render(request, 'adaugaprogramare.html', context)


def adaugaprogramarepacient(request):
    pacienti = Pacient.objects
    medici = Medic.objects
    asistenti = Asistent.objects
    form = FormModelProgramarePacient(request.POST)
    if form.is_valid():
        form.save()
        pacient = form.cleaned_data['pacient']
        medic = form.cleaned_data['medic']
        asistent = form.cleaned_data['asistent']
        data_si_ora = form.cleaned_data['data_si_ora']
        durata_in_minute = form.cleaned_data['durata_in_minute']
        notes = form.cleaned_data['notes']
        status = form.cleaned_data['status']
        form = FormModelProgramarePacient()
        return HttpResponse('Programarea a fost adaugată cu succces așteaptă confirmarea acesteia!')
    form = FormModelProgramarePacient()
    context = {'pacienti':pacienti,'medici':medici,'asistenti':asistenti, 'form':form}
    return render(request, 'adaugaprogramarepacient.html', context)

def adaugafisa(request):
    pacienti = Pacient.objects
    diagnostice = Diagnostic.objects
    tratamente = Tratament.objects
    facturi = Factura.objects
    form = FormModelFisa(request.POST)
    if form.is_valid():
        form.save()
        pacient = form.cleaned_data['pacient']
        programare = form.cleaned_data['programare']
        diagnostic = form.cleaned_data['diagnostic']
        tratament = form.cleaned_data['tratament']
        factura = form.cleaned_data['factura']
        notes = form.cleaned_data['notes']
        status = form.cleaned_data['status']
        form = FormModelFisa()
        return HttpResponse('Fisa pacientului a fost adaugată cu succces !')
    form = FormModelFisa()
    context = {'pacienti':pacienti,'diagnostice':diagnostice,'tratamente':tratamente, 'facturi':facturi, 'form':form}
    return render(request, 'adaugafisa.html', context)

def adaugaprodus(request):
    parteneri = Partener.objects

    form = FormModelProdus(request.POST)
    if form.is_valid():
        form.save()
        denumire = form.cleaned_data['denumire']
        cantitate = form.cleaned_data['cantitate']
        data_de_expirare = form.cleaned_data['data_de_expirare']
        unitate_de_masura = form.cleaned_data['unitate_de_masura']
        distribuitor = form.cleaned_data['distribuitor']
        pret_unitar = form.cleaned_data['pret_unitar']
        notes = form.cleaned_data['notes']
        status = form.cleaned_data['status']
        form = FormModelProdus()
        return HttpResponse('Produsul a fost adaugat cu succces !')
    form = FormModelProdus()
    context = {'parteneri':parteneri, 'form':form}
    return render(request, 'adaugaprodus.html', context)

def adaugafactura(request):
    pacienti = Pacient.objects
    produse = Produs.objects
    tratamente = Tratament.objects
    form = FormModelFactura(request.POST)
    if form.is_valid():
        form.save()
        numar_factura = form.cleaned_data['numar_factura']
        serie_factura =  form.cleaned_data['serie_factura']
        emitent = form.cleaned_data['emitent']
        pacient = form.cleaned_data['pacient']
        produs = form.cleaned_data['produs']
        cantitate = form.cleaned_data['cantitate']
        tratament = form.cleaned_data['tratament']
        data_emitere = form.cleaned_data['data_emitere']
        notes = form.cleaned_data['notes']
        status = form.cleaned_data['status']
        form = FormModelFactura()
        return HttpResponse('Factura a fost adaugată cu succces !')
    form = FormModelFactura()
    context = {'pacienti':pacienti,'produse':produse,'tratamente':tratamente, 'form':form}
    return render(request, 'adaugafactura.html', context)

def adaugadiagnostic(request):
    form = FormModelDiagnostic(request.POST)
    if form.is_valid():
        form.save()
        denumire = form.cleaned_data['denumire']
        notes = form.cleaned_data['notes']
        status = form.cleaned_data['status']
        form = FormModelDiagnostic()
        return HttpResponse('Diagnosticul a fost adaugat cu succces !')
    form = FormModelDiagnostic()
    context = {'form':form}
    return render(request, 'adaugadiagnostic.html', context)

def adaugatratament(request):
    form = FormModelTratament(request.POST)
    if form.is_valid():
        form.save()
        denumire = form.cleaned_data['denumire']
        produs = form.cleaned_data['produs']
        cantitate = form.cleaned_data['cantitate']
        notes = form.cleaned_data['notes']
        status = form.cleaned_data['status']
        form = FormModelTratament()
        return HttpResponse('Tratamentul a fost adaugat cu succces !')
    form = FormModelTratament()
    context = {'form':form}
    return render(request, 'adaugatratament.html', context)

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

def alege_medic(val, medic):
    if val == "Implantologie":
        if medic.specializare == 'Implantologie':
            return medic
