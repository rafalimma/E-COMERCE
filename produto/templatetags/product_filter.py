from django.template import Library
from utils import utils

register = Library()

@register.filter
def formata_preco(val):
    return f'R$ {val:.2f}'.replace('.', ',')

@register.filter
def card_total_qtd(carrinho):
    return utils.card_total_qtd(carrinho)