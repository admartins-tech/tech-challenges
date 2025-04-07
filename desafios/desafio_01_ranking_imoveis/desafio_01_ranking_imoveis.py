"""
Script de ranking de imóveis por preço para o setor imobiliário.

Objetivo:
    - Ordenar uma lista de imóveis do mais barato para o mais caro.
    - Exibir o ranking formatado, com valores no padrão monetário brasileiro.

Contexto:
    - Exemplo de aplicação prática voltado para desafios do QuintoAndar.
    - Demonstra prática de funções, ordenação de listas e formatação de saída.
"""

def ordenar_imoveis(imoveis):
    """
    Ordena a lista de imóveis pelo preço em ordem crescente.

    Args:
        imoveis (list): Lista de dicionários com informações dos imóveis.

    Returns:
        list: Lista de imóveis ordenada do mais barato para o mais caro.
    """
    return sorted(imoveis, key=lambda imovel: imovel['preco'])


def exibir_ranking(imoveis):
    """
    Exibe o ranking dos imóveis formatado para visualização do cliente.

    Args:
        imoveis (list): Lista de imóveis ordenados por preço.
    """
    for index, imovel in enumerate(imoveis, start=1):
        preco_formatado = f"R${imovel['preco']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        print(f"{index}. Endereço: {imovel['endereco']} - Preço: {preco_formatado}")


imoveis = [
    {"endereco": "Apartamento Bela Vista", "preco": 3000},
    {"endereco": "Studio Centro", "preco": 2000},
    {"endereco": "Casa Jardim Europa", "preco": 5000}
]

imoveis_ordenados = ordenar_imoveis(imoveis)
exibir_ranking(imoveis_ordenados)