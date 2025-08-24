from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
# Create your views here.


class Pagar(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de pagamento")


class FecharPedido(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de fechamento de pedido")


class Detalhe(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de detalhes do pedido")

    pass
