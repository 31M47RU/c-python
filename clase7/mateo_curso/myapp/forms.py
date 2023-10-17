from django import forms

class AddCurse(forms.Form):
    name = forms.CharField(max_length=30, label='Nombre de alumno')