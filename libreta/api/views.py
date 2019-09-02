from rest_framework import viewsets
from ..models import Familia,Companeros_trabajo
from .serializers import FamiliaSerializer, TrabajoSerializer

class FamiliaViewset(viewsets.ModelViewSet):
    """
    vista para obtener (get) todos los contactos de familia
    y tambien para poder crearlos (post)
    """
    queryset = Familia.objects.all()
    serializer_class = FamiliaSerializer

class TrabajoViewset(viewsets.ModelViewSet):
    """
    vista para obtener (get) todos los contactos de trabajo
    y tambien para poder crearlos (post)
    """
    queryset = Companeros_trabajo.objects.all()
    serializer_class = TrabajoSerializer