from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View,ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FamiliaForm, TrabajoForm
from .models import Familia,Companeros_trabajo

class MainView(View):
    """
    vista para renderear menu de
    contactos
    """
    def get(self,request):
        template_name = 'main.html'
        return render(request,template_name)

class LibretaView(ListView):
    """
    vista genérica para ver 
    lista de contactos
    """
    model = Familia

class LibretaCreateView(CreateView):
    """
    vista genérica para crear un
    nuevo contacto
    """
    model = Familia
    form_class = FamiliaForm
    success_url = reverse_lazy('list_libreta_familia')

class LibretaUpdateView(UpdateView):
    """
    vista genérica para editar
    un contacto existente
    """
    model = Familia
    form_class = FamiliaForm
    success_url = reverse_lazy('list_libreta_familia')

class LibretaDeleteView(DeleteView):
    """
    vista genérica para borrar un
    contacto
    """
    model = Familia
    success_url = reverse_lazy('list_libreta_familia')

class TrabajoView(ListView):
    """
    vista genérica para ver 
    lista de contactos de trabajo
    """
    model = Companeros_trabajo

class TrabajoCreateView(CreateView):
    """
    vista genérica para crear un
    nuevo contacto de trabajo
    """
    model = Companeros_trabajo
    form_class = TrabajoForm
    success_url = reverse_lazy('list_libreta_trabajo')

class TrabajoUpdateView(UpdateView):
    """
    vista genérica para editar
    un contacto existente de trabajo
    """
    model = Companeros_trabajo
    form_class = TrabajoForm
    success_url = reverse_lazy('list_libreta_trabajo')

class TrabajoDeleteView(DeleteView):
    """
    vista genérica para borrar un
    contacto de trabajo
    """
    model = Companeros_trabajo
    success_url = reverse_lazy('list_libreta_trabajo')
