from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FamiliaForm
from .models import Familia

class Libreta(ListView):
    """
    vista generica para ver 
    lista de contactos
    """
    model = Familia

class LibretaCreateView(CreateView):
    """
    vista generica para crear un
    nuevo contacto
    """
    model = Familia
    form_class = FamiliaForm
    success_url = reverse_lazy('list_libreta_familia')

class LibretaUpdateView(UpdateView):
    """
    vista generica para editar
    un contacto existente
    """
    model = Familia
    form_class = FamiliaForm
    success_url = reverse_lazy('list_libreta_familia')

class LibretaDeleteView(DeleteView):
    """
    vista generica para borrar un
    contacto
    """
    model = Familia
    success_url = reverse_lazy('list_libreta_familia')
