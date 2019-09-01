from django.db import models
from django.conf import settings


class Usuario(models.Model):
    """
    Modelo que especifica los campos necesarios para registrar un 
    nuevo usuario
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    telefono = models.CharField(max_length=10,blank=True,null=True)
    
    def __str__(self):
        return 'Perfil del usuario {}'.format(self.user.username)