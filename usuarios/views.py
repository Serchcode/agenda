from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Usuario
from django.contrib import messages
from .forms import UserRegistrationForm


class Index(View):
    """
    Vista index
    """
    def get(self, request):
        """
        funcion para mostrar index
        """
        template_name = "index.html"
        return render(request,template_name)

class Registration(View):
    """
    Vista necesaria para relizar registro
    de un nuevo usuario
    """
    def get(self, request):
        """
        funcion para mostrar el formulario dentro de nuestro
        template
        """
        template_name = "registration.html"
        form = UserRegistrationForm()
        context = {
            'form':form,
        }
        return render(request,template_name,context)
    
    def post(self,request):
        """
        funcion que resive en el request los datos proporcionados
        en el formulario de registro
        """
        template_name = "registration.html"
        new_user_form = UserRegistrationForm(request.POST)
        data_user = request.POST
        if new_user_form.is_valid():
            new_user = new_user_form.save(commit=False)
            new_user.set_password(new_user_form.cleaned_data['password'])
            new_user.save()
            perfil = Usuario()
            perfil.user = new_user
            perfil.save()
            messages.success(request,"Su registro fue exitoso.")
            return redirect('login')
        else:
            context = {
                'form':new_user_form
            }
            return render(request,template_name,context)