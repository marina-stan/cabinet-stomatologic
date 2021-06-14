from django import forms
from django.conf import settings
from django.core.cache import cache
from django.contrib.admin import widgets
from django.shortcuts import get_object_or_404

class contactformemail(forms.Form):
	fromemail=forms.EmailField(required=True)
	subject=forms.CharField(required=True)
	body=forms.CharField(widget=forms.Textarea, required=True)
	uploaded_file = forms.FileField(required = False)
