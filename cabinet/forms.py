from django import forms

class contactformemail(forms.Form):
	fromemail=forms.EmailField(required=True)
	subject=forms.CharField(required=True)
	body=forms.CharField(widget=forms.Textarea, required=True)
