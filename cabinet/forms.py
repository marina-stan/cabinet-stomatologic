from django import forms
from django.conf import settings
from django.core.cache import cache
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from django.shortcuts import get_object_or_404
from managementcabinet.models import Person
from managementcabinet.models import Pacient
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
