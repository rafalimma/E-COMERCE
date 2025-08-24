from django.shortcuts import render

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
# Create your views here.

class Criar(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de criação de perfil")

class Login(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de login")

class Atualizar(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de atualização de perfil")

class Logout(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de logout")
