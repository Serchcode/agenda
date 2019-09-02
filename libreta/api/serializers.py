from ..models import Familia, Companeros_trabajo
from rest_framework import serializers

class FamiliaSerializer(serializers.ModelSerializer):
    """
    serializador para modelo de contactos de familia
    """
    class Meta:
        model = Familia
        fields = '__all__'

class TrabajoSerializer(serializers.ModelSerializer):
    """
    serializador para modelo de contactos de trabajo
    """
    class Meta:
        model = Companeros_trabajo
        fields = '__all__'