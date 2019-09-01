from django.db import models

# Create your models here.

class Familia(models.Model):
    """
    Modelo que específica los campos necesarios para registrar un
    nuevo contacto familiar
    """

    OPCIONES = (('familiar','familiar'),
                ('amigo','amigo'),)

    nombre = models.CharField(max_length=10,blank=True,null=True, verbose_name='Nombre')
    apellido_paterno = models.CharField(max_length=10,blank=True,null=True, verbose_name='Apellido paterno')
    apellido_materno = models.CharField(max_length=10,blank=True,null=True, verbose_name='Apellido materno')
    telefono = models.CharField(max_length=10,blank=True,null=True, verbose_name='Teléfono')
    domicilio = models.CharField(max_length=50,blank=True,null=True, verbose_name='Domicilio')
    status = models.CharField(choices=OPCIONES,max_length=10,blank=True,null=True, verbose_name='Amigo/Familiar')

    def __str__(self):
        return '{}'.format(self.nombre)


class Companeros_trabajo(models.Model):
    """
    Modelo que específica los campos neesarios para registrar un 
    nuevo contacto de trabajo
    """

    OPCIONES_AREA = (('areaA','Área A'),
                ('areaB','Área B'),)

    nombre = models.CharField(max_length=10,blank=True,null=True, verbose_name='Nombre')
    apellido_paterno = models.CharField(max_length=10,blank=True,null=True, verbose_name='Apellido paterno')
    apellido_materno = models.CharField(max_length=10,blank=True,null=True, verbose_name='Apellido materno')
    telefono = models.CharField(max_length=10,blank=True,null=True, verbose_name='Teléfono')
    domicilio = models.CharField(max_length=50,blank=True,null=True, verbose_name='Domicilio')
    empresa = models.CharField(max_length=10,blank=True,null=True, verbose_name='Empresa')
    area = models.CharField(choices=OPCIONES_AREA,max_length=10,blank=True,null=True, verbose_name='Área')
    rubro_empresa = models.CharField(max_length=10,blank=True,null=True, verbose_name='Rubro empresa')

    def __str__(self):
        return '{}'.format(self.nombre)