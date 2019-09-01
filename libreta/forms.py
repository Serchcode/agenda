from django import forms
from django.forms import ModelForm
from .models import Familia, Companeros_trabajo


class FamiliaForm(ModelForm):
    """
    formulario proporcionado para registrar un nuevo
    contacto familiar
    """
    class Meta:
        model = Familia
        fields = '__all__'

class TrabajoForm(ModelForm):
    """
    formulario proporcionado para registrar un nuevo
    contacto de trabajo
    """
    class Meta:
        model = Companeros_trabajo
        fields = '__all__'