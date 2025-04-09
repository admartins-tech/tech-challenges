import calendar

# Lista de imóveis simulados com valores mensais fixos, para permitir a seleção dinâmica pelo usuário.
imoveis = {"Imóvel A": 3000, "Imóvel B": 25000, "Imóvel C": 2000}

def coletar_dados():
    """
    Coleta as informações necessárias do usuário para realizar o cálculo.
    Perguntamos esses dados porque são essenciais para personalizar o cálculo do aluguel proporcional,
    garantindo que a simulação reflita a realidade da data e do imóvel escolhido.
    
    Returns:
        tuple: nome do cliente, imóvel escolhido, e data de entrada no imóvel.
    """
    nome = input("Qual o seu nome? ")
    imovel_alugado = input("Informe qual imóvel foi alugado: ") 
    data_entrada = input("Quando você pretende se mudar? Nos informe a data (contendo o dia, mês e o ano, exemplo: 03/07/2025) ")
    return nome, imovel_alugado, data_entrada

def converter_data_para_inteiros(data_entrada):
    """
    Converte a data de entrada para inteiros para facilitar o cálculo.
    Fazemos isso porque a biblioteca calendar e operações aritméticas de datas requerem números inteiros,
    e o input do usuário vem como string separada por '/'.
    
    Args:
        data_entrada (str): Data no formato "DD/MM/AAAA".
    
    Returns:
        tuple: dia, mês e ano como inteiros.
    """
    dia, mes, ano = map(int, data_entrada.split('/'))
    return dia, mes, ano

def obter_dias_do_mes(ano, mes):
    """
    Determina o total de dias no mês da entrada do usuário.
    Isso garante que o cálculo do valor proporcional de aluguel considere corretamente meses com diferentes quantidades de dias,
    como fevereiro ou meses de 31 dias, aumentando a precisão do cálculo.
    
    Args:
        ano (int): Ano da data de entrada.
        mes (int): Mês da data de entrada.
    
    Returns:
        int: Quantidade de dias no mês.
    """
    dias_do_mes = calendar.monthrange(ano, mes)[1]
    return dias_do_mes

def consultar_valor_do_aluguel(imoveis, imovel_alugado):
    """
    Consulta o valor mensal do aluguel com base na escolha do usuário.
    Garantimos que o cálculo esteja atrelado ao imóvel correto e à tabela de valores simulada.
    
    Args:
        imoveis (dict): Dicionário com imóveis e valores de aluguel.
        imovel_alugado (str): Imóvel escolhido pelo usuário.
    
    Returns:
        int: Valor mensal do aluguel.
    """
    valor_do_aluguel = imoveis[imovel_alugado]
    return valor_do_aluguel

def calcular_valor_proporcional(dias_do_mes, valor_do_aluguel, dia):
    """
    Calcula o valor proporcional do aluguel considerando a data de entrada no imóvel.
    Fazemos isso para cobrar apenas pelos dias efetivamente utilizados no mês de entrada,
    garantindo uma simulação mais justa e profissional para o cliente.
    
    Args:
        dias_do_mes (int): Total de dias no mês de entrada.
        valor_do_aluguel (int): Valor mensal do aluguel do imóvel.
        dia (int): Dia de entrada no imóvel.
    
    Returns:
        float: Valor proporcional do aluguel.
    """
    valor_por_dia = valor_do_aluguel / dias_do_mes
    dias_considerados = dias_do_mes - dia + 1  # Incluímos o dia da mudança
    valor_proporcional = valor_por_dia * dias_considerados
    return valor_proporcional

def formatar_valor_proporcional(valor_proporcional):
    """
    Formata o valor proporcional calculado para o padrão brasileiro de moeda.
    Fazemos isso para melhorar a experiência do usuário e entregar uma resposta amigável e clara,
    evitando confusões com separadores decimais.
    
    Args:
        valor_proporcional (float): Valor bruto calculado.
    
    Returns:
        str: Valor formatado como moeda.
    """
    valor_proporcional_formatado = f"R$ {valor_proporcional:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    return valor_proporcional_formatado

def responder_usuario(nome, imovel_alugado, data_entrada, valor_proporcional_formatado):
    """
    Exibe o resultado final para o usuário de forma clara e personalizada.
    Personalizamos a mensagem para tornar a experiência mais amigável e profissional,
    mostrando o valor proporcional calculado.
    
    Args:
        nome (str): Nome do usuário.
        imovel_alugado (str): Imóvel selecionado pelo usuário.
        data_entrada (str): Data de entrada no imóvel.
        valor_proporcional_formatado (str): Valor proporcional formatado.
    """
    print(f"Entendi, {nome}! Para o {imovel_alugado}, considerando a data de entrada {data_entrada}, o valor proporcional será de {valor_proporcional_formatado}.")

def executar_programa():
    """
    Função principal que executa o fluxo completo do programa.
    Reúne todas as etapas para realizar o cálculo e entregar o resultado final ao cliente.
    """
    nome, imovel_alugado, data_entrada = coletar_dados()
    dia, mes, ano = converter_data_para_inteiros(data_entrada)
    dias_do_mes = obter_dias_do_mes(ano, mes)
    valor_do_aluguel = consultar_valor_do_aluguel(imoveis, imovel_alugado)
    valor_proporcional = calcular_valor_proporcional(dias_do_mes, valor_do_aluguel, dia)
    valor_proporcional_formatado = formatar_valor_proporcional(valor_proporcional)
    responder_usuario(nome, imovel_alugado, data_entrada, valor_proporcional_formatado)

# Inicia o programa
executar_programa()