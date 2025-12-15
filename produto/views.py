from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
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

class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produtos'
    slug_url_kwarg = 'slug'

class AdicionarCarrinho(View):
    def get(self, request, *args, **kwargs):
        print('entroi na função')
        http_referrer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produtos:lista')
        )
        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            messages.error(
                self.request,
                'produto não existe'
            )
            return redirect(http_referrer)
        
        variacao = get_object_or_404(models.Variacao, id=variacao_id)
        produto = variacao.produto
        produto_id = produto.id
        produto_nome = produto.nome
        variacao_nome = variacao.nome or ''
        variacao_id = variacao.id
        preco_unitario = variacao.preco
        preco_unitario_promocional = variacao.preco_promocional
        quantidade = 1
        imagem = produto.imagem

        if variacao.estoque < 1:
            messages.error(self.request, 'Estoque insuficiente')
            return redirect(http_referrer)
        
        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()
        
        carrinho = self.request.session['carrinho']
        if variacao_id in carrinho:
            # TODO Variação existe no carrinho
            pass
        else:
            carrinho[variacao_id] = {
                produto_id : produto_id,
                'produto_nome' : produto_nome,
                'variacao_nome' : variacao_nome,
                'variacao_id' : variacao_id,
                'preco_unitario' : preco_unitario,
                'preco_unitario_promocional' : preco_unitario_promocional
                'quantidade' : 1
                'imagem' : produto_imagem
            }

        return HttpResponse('Adicionar carrinho')

class RemoverCarrinho(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de remover do carrinho")

class Carrinho(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página do carrinho")

class Finalizar(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de finalização de compra")
