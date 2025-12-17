def card_total_qtd(carrinho):
    return sum([item['quantidade'] for item in carrinho.values])