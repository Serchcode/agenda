from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('registro/', views.Registration.as_view(), name='registro'),
]
