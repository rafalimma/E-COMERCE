from django.shortcuts import render

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import forms
from . import models
# Create your views here.

class BasePerfil(View):
    template_name = 'criar.html'
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)


        if self.request.user.is_authenticated:
            self.perfil = models.Perfil.objects.filter(
                usuario=self.request.user).first()
            self.contexto = {
                'userform' : forms.UserForm(
                    data=self.request.POST or None,
                    usuario=self.request.user,
                    instance=self.request.user,
                    ),
                'perfilform' : forms.PerfilForm(data=self.request.POST or None)
            }

            self.renderizar = render(
                self.request, self.template_name, self.contexto
            )
        else:
            self.contexto = {
                'userform' : forms.UserForm(data=self.request.POST or None),
                'perfilform' : forms.PerfilForm(data=self.request.POST or None)
            }

            self.userform = self.contexto['userform']
            self.perfilform = self.contexto['perfilform']

            self.renderizar = render(
                self.request, self.template_name, self.contexto
            )

    def get(self, request, *args, **kwargs):
        return self.renderizar
    


class Criar(BasePerfil):
    def post(self, *args, **kwargs):
        if not self.userform.is_valid() or not self.perfilform.is_valid():
            print('invalido')
            return self.renderizar
        if self.request.user.is_authenticated:
            pass
        else:
            usuario = self.userform.save
        return self.renderizar

class Login(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de login")

class Atualizar(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de atualização de perfil")

class Logout(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de logout")
