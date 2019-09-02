from rest_framework import routers
from django.conf.urls import include, re_path
from django.urls import path
from libreta.api.views import FamiliaViewset,TrabajoViewset


router = routers.DefaultRouter()
router.register(r'contactos-familia/', FamiliaViewset)
router.register(r'contactos-trabajo', TrabajoViewset)

urlpatterns = [
    re_path('^contactos/', include(router.urls)),
]