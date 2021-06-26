from django import forms
from django.conf import settings
from django.core.cache import cache
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from django.shortcuts import get_object_or_404

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
