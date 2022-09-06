"""
    Universidade Federal Rural do Semi-Árido
    Departamento de Engenharia e Tecnologia

    AMB1430 - Programação para Engenharia Elétrica
    Periodo 2022.1 - bruno.luna@ufersa.edu.br

    Atividade Sincrona I - Potência em Sistemas de Corrente Alternada

    Leia o código e busque pelo termo <TODO> para executar as atividades

    Realize a leitura das seguintes referências

        Usando Python como uma calculadora
        https://docs.python.org/pt-br/3/tutorial/introduction.html#using-python-as-a-calculator

        Mais ferramentas de controle de fluxo
        https://docs.python.org/pt-br/3/tutorial/controlflow.html

        Definindo funções
        https://docs.python.org/pt-br/3/tutorial/controlflow.html#defining-functions

        Expressões lambda
        https://docs.python.org/pt-br/3/tutorial/controlflow.html#lambda-expressions

        Strings de documentação (docstring)
        https://docs.python.org/pt-br/3/tutorial/controlflow.html#tut-docstrings

        Compreensões de lista
        https://docs.python.org/pt-br/3/tutorial/datastructures.html#list-comprehensions

        Compreensões de lista aninhadas
        https://docs.python.org/pt-br/3/tutorial/datastructures.html#nested-list-comprehensions

        Técnicas de iteração
        https://docs.python.org/pt-br/3/tutorial/datastructures.html#looping-techniques

        Mais sobre listas (append)
        https://docs.python.org/pt-br/3/tutorial/datastructures.html#more-on-lists
"""

from math import *


def senoide(amplitude, frequencia, fase, t):
    """ Simulação de uma forma de onda senoidal

    .. math::
        A Sin(2 \\pi f t + \\theta)

    Args:
        amplitude (float): valor de pico da forma de onda senoidal
        frequencia (float): frequência da forma de onda senoidal
        fase (float): fase da forma de onda senoidal
        t (float): instante de tempo da amostra

    Returns:
        (float): valor da forma de onda senoidal no instante t
    """
    return amplitude * sin(2 * pi * frequencia * t + fase)


def valor_medio(forma_de_onda):
    """ Tensão média de uma forma de onda senoidal

    .. math::
        \\sum_{n} v(n)/n_{max}

    Args:
        forma_de_onda (list): lista de amostras da forma de onda senoidal

    Return:
        (float): valor médio
    """
    return sum(forma_de_onda) / len(forma_de_onda)


def valor_eficaz(forma_de_onda):
    """ Tensão eficaz de uma forma de onda senoidal

    .. math::
        \\sqrt{\\sum_{n} v(n)^{2}/n}

    Algoritmo para o calculo da tensão eficaz
        quadrado das amostras de tensão
            lambda amostra: amostra * amostra (amostra = amostra**2)
        soma acumulada dos quadrados das amostras de tensão
        divisao da soma acumulada pelo numero de amostras de tensão
        raiz quadrada do resultado da divisão

    Args:
        forma_de_onda (list): lista de amostras da forma de onda senoidal

    Returns:
        (float): valor eficaz
    """
    return sqrt(sum(map(lambda amostra: amostra*amostra, forma_de_onda)) / len(forma_de_onda))


def frequencia(forma_de_onda, passo_de_simulacao):
    """ Frequência de uma forma de onda senoidal

    TODO: DESCREVA O ALGORITMO PARA O CÁLCULO DA FORMA DE ONDA

    Args:
        forma_de_onda (list): lista de amostras da forma de onda senoidal
        passo_de_simulacao (float): passo de cáculo de simulação ou periodo de amostragem

    Return:
        (float): frequência estimada
    """
    # TODO: DESCREVA O CÓDIGO DA FUNÇÃO
    #       SE NECESSÁRIO, COMENTE AS LINHAS (#) E EXECUTE O CÓDIGO PARCIALMENTE
    #       OU UTILIZE A FUNÇÃO PRINT PARA DIAGNÓSTICO (DEBUG)
    # TODO: REESCREVA O CÓDIGO DA FUNÇÃO PARA APRESENTAR MAIOR CLAREZA E MENOS COMENTÁRIOS
    zeros = []
    frequencia_estimada = 0
    cruzamento_por_zero = 0
    ultimo_cruzamento_por_zero = 0

    for amostra in range(len(forma_de_onda)):
        if forma_de_onda[amostra] > 0:
            cruzamento_por_zero = 1
        else:
            cruzamento_por_zero = 0

        if cruzamento_por_zero != ultimo_cruzamento_por_zero:
            zeros.append(amostra)
            ultimo_cruzamento_por_zero = cruzamento_por_zero
            cruzamento_por_zero = ~ cruzamento_por_zero

    for posicao in range(len(zeros) - 1):
        frequencia_estimada += 1 / (2 * passo_de_simulacao * (zeros[posicao + 1] - zeros[posicao]))

    frequencia_estimada /= posicao + 1

    return frequencia_estimada


def main():
    """ Função Principal """

    # Parâmetros das formas de onda senoidais
    amplitude_tensao = 100.0
    frequencia_tensao = 60.0
    angulo_de_fase_tensao = radians(0.0)
    amplitude_corrente = 10.0
    frequencia_corrente = frequencia_tensao
    angulo_de_fase_corrente = radians(0.0)

    # Parâmetros de simulação
    tempo_de_simulacao = 1.0
    passo_de_simulacao = 100e-6
    numero_de_amostras = int(tempo_de_simulacao / passo_de_simulacao)
    # Instantes de amostragem
    t = [passo_de_simulacao * t for t in range(numero_de_amostras)]

    # Listas das amostras de tensao e corrente
    tensao = []
    corrente = []
    for amostra in range(numero_de_amostras):
        tensao.append(senoide(amplitude_tensao, frequencia_tensao, angulo_de_fase_tensao, t[amostra]))
        corrente.append(senoide(amplitude_corrente, frequencia_corrente, angulo_de_fase_corrente, t[amostra]))

    # -------------------------------------------------------------------------
    # CÁLCULO DE POTÊNCIA EM SISTEMAS DE CORRENTE ALTERNADA
    # -------------------------------------------------------------------------
    # TODO: ESCREVA UMA FUNÇÃO PARA O CÁLCULO DO VALOR DE PICO DAS FORMAS DE ONDA
    # TODO: ESCREVA UMA FUNÇÃO PARA SUBTRAIR O VALOR MÉDIO DAS LISTAS ANTES DO CÁLCULO DOS VALORES EFICAZES
    tensao_media = valor_medio(tensao)
    corrente_media = valor_medio(corrente)
    # Escrever e inserir a função para subtração do valor médio das listas de tensao e corrente
    tensao_eficaz = valor_eficaz(tensao) # utilizar a lista sem o valor médio
    corrente_eficaz = valor_eficaz(corrente) # utilizar a lista sem o valor médio
    # Escrever e inserir a função para o cálculo do valor de pico das listas de tensao e corrente
    frequencia_media = 0.0 # frequencia(tensao, passo_de_simulacao)

    # TODO: ESCREVA AS FUNÇÕES PARA O CÁLCULO DAS POTENCIAS (ATIVA, REATIVA E APARENTE)
    # TODO: ESCREVA AS FUNÇÕES PARA O CÁLCULO DO FATOR DE POTÊNCIA E DO ÂNGULO DE FASE
    # TODO: ESCREVA OU REESCREVA A DOCUMENTAÇÃO DE TODAS AS FUNÇÕES (docstring)
    # TODO: TESTE AS FUNÇÕES PARA VALORES DIFERENTES DE AMPLITUDE E FREQUÊNCIA E COMENTE OS RESULTADOS
    # TODO: TESTE AS FUNÇÕES PARA VALORES DIFERENTES DO ANGULO DE FASE E COMENTE OS RESULTADOS
    potencia_aparente = tensao_eficaz * corrente_eficaz
    potencia_ativa = sum(
        [amostra_tensao * amostra_corrente for amostra_tensao, amostra_corrente in zip(tensao, corrente)]) / len(tensao)
    potencia_reativa = sqrt(potencia_aparente ** 2 - potencia_ativa ** 2)
    fator_de_potencia = potencia_ativa / potencia_aparente
    angulo_de_fase = degrees(acos(fator_de_potencia))
    # TODO: OS SEGUINTES DESAFIOS NÃO SÃO OBRIGATÓRIOS
    # TODO: DESAFIO 1 - ESCREVAS NOVAS FUNÇÕES PARA O CÁLCULO A CADA <frequencia> PERIODOS DA FORMA DE ONDA
    # TODO: DESAFIO 2 - ESCREVAS NOVAS FUNÇÕES SEM UTILIZAR LISTAS COMO PARÂMETROS OU COMO RETORNO
    #                   CADA FUNÇÃO DEVE RECEBER APENAS O VALOR DE UMA AMOSTRA E RETORNAR O VALOR CALCULADO
    # -------------------------------------------------------------------------

    # Apresentacao dos resultados
    print(f"""
        Potência em sistema de corrente alternada

        Tensão eficaz     : {tensao_eficaz:10.2f} [V]
        Tensão pico       : {tensao_eficaz * sqrt(2):10.2f} [V]
        Tensão média      : {tensao_media:10.2f} [V]
        Frequência        : {frequencia_media:10.2f} [Hz]

        Corrente eficaz   : {corrente_eficaz:10.2f} [Arms]
        Corrente pico     : {corrente_eficaz * sqrt(2):10.2f} [A]
        Corrente média    : {corrente_media:10.2f} [A]

        Potência ativa    : {potencia_ativa:10.2f} [W]
        Potência reativa  : {potencia_reativa:10.2f} [Var]
        Potência aparente : {potencia_aparente:10.2f} [VA]
        Fator de potência : {fator_de_potencia:10.2f}
        Ângulo de fase    : {angulo_de_fase:10.2f} [graus]
        """)

    print(frequencia(tensao, passo_de_simulacao))


if __name__ == "__main__":
    """ Modulo """
    main()
