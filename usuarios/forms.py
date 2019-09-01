from django import forms
from django.contrib.auth.models import User
from .models import Usuario

class UserRegistrationForm(forms.ModelForm):
    """
	formulario necesario para registar un nuevo
	usuario
	"""
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite tu password',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name')
        
    def clean_password2(self):
        """
        funcićon para verificar que el password sea correcto
        """
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Los passwords no coicinden')
        return cd['password2']