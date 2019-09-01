from django import forms
from django.forms import ModelForm
from .models import Familia


class FamiliaForm(ModelForm):
    """
    formulario proporcionado para registrar un nuevo
    contacto familiar
    """
    class Meta:
        model = Familia
        fields = '__all__'
