from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginated_by = 10

class DetalheProduto(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de detalhes do produtorvrevebtebrtnbrt")

class AdicionarCarrinho(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de adicionar ao carrinho")

class RemoverCarrinho(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de remover do carrinho")

class Carrinho(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página do carrinho")

class Finalizar(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de finalização de compra")
