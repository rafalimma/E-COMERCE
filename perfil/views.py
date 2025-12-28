from django.shortcuts import render

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import forms
# Create your views here.

class BasePerfil(View):
    template_name = 'criar.html'
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.contexto = {
            'userform' : forms.UserForm(data=self.request.POST or None),
            'perfilform' : forms.PerfilForm(data=self.request.POST or None)
        }

        self.renderizar = render(
            self.request, self.template_name, self.contexto
        )

    def get(self, request, *args, **kwargs):
        return self.renderizar
    


class Criar(BasePerfil):
    pass

class Login(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de login")

class Atualizar(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de atualização de perfil")

class Logout(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de logout")
