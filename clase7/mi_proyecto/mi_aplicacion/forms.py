# en tus forms.py
from django import forms
from .models import Entidad

class EntidadForm(forms.ModelForm):
    class Meta:
        model = Entidad
        fields = ['nombre', 'descripcion']  # Ajusta los campos según tu modelo
