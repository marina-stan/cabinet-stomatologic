from django import forms
from django.conf import settings
from django.core.cache import cache
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from django.shortcuts import get_object_or_404
from managementcabinet.models import Person
from managementcabinet.models import Pacient
from managementcabinet.models import Medic
from managementcabinet.models import Asistent
from managementcabinet.models import Programare
from managementcabinet.models import Diagnostic
from managementcabinet.models import Tratament
from managementcabinet.models import Factura
from managementcabinet.models import FisaPacient
from managementcabinet.models import models
from django.contrib.auth.models import User

class contactformemail(forms.Form):
	fromemail=forms.EmailField(required=True)
	subject=forms.CharField(required=True)
	body=forms.CharField(widget=forms.Textarea, required=True)
	uploaded_file = forms.FileField(required = False)

class DateInput(forms.DateInput):
	input_type = 'datetime-local'

class DateForm(forms.Form):
	date = forms.DateTimeField(widget=DateInput)

	def cleandate(self):
	    c_date=self.cleaned_data['date']
	    if c_date < datetime.date.today():
	        raise ValidationError(_('Data introdusă a trecut'))
	    elif c_date > datetime.date.today():
	        return date

class ModelDateForm(forms.Form):
	class Meta:
		widgets = {'date':DateInput}


class FormModelPacient(forms.ModelForm):
	nume_de_familie = models.CharField()
	prenume = models.CharField()
	cnp = models.CharField()
	email = models.EmailField()
	numar_de_telefon = models.CharField()
	adresa = models.TextField()
	note = models.TextField()
	persoana_de_contact = models.CharField()
	status = models.BooleanField()

	class Meta:
		model = Pacient
		fields = ('nume_de_familie', 'prenume', 'cnp', 'email', 'numar_de_telefon', 'adresa', 'note', 'persoana_de_contact', 'status')


class FormModelProgramare(forms.ModelForm):
	pacient = Pacient(forms.ModelMultipleChoiceField(queryset=Pacient.objects.all()))
	medic = Medic(forms.ModelMultipleChoiceField(queryset=Medic.objects.all()))
	asistent = Asistent(forms.ModelMultipleChoiceField(queryset=Asistent.objects.all()))
	data_si_ora = models.DateTimeField()
	durata_in_minute = models.PositiveSmallIntegerField()
	notes = models.TextField()
	status = models.BooleanField()

	class Meta:
		model = Programare
		fields = ('pacient', 'medic', 'asistent', 'data_si_ora', 'durata_in_minute', 'notes', 'status')


class FormModelFisa(forms.ModelForm):
	pacient = Pacient(forms.ModelMultipleChoiceField(queryset=Pacient.objects.all()))
	programare = Programare(forms.ModelMultipleChoiceField(queryset=Programare.objects.all()))
	diagnostic = Diagnostic(forms.ModelMultipleChoiceField(queryset=Diagnostic.objects.all()))
	tratament = Tratament(forms.ModelMultipleChoiceField(queryset=Tratament.objects.all()))
	factura = Factura(forms.ModelMultipleChoiceField(queryset=Factura.objects.all()))
	notes = models.TextField()
	status = models.BooleanField()

	class Meta:
		model = FisaPacient
		fields = ('pacient', 'programare', 'diagnostic', 'tratament', 'factura', 'notes', 'status')
