import random

class SorteadorBingo:
    """
    * Esta classe gerencia um sorteador de Bingo, controlando os números
    * sorteados, os números restantes e o estado geral do jogo.
    """

    def __init__(self, qtd_numeros=75):
        self.__qtd_numeros = qtd_numeros
        self.__numeros = list(range(1, qtd_numeros + 1))
        self.__bolinhas_sorteadas = []
        self.__qtd_bolinhas_sorteadas = 0
        self.__qtd_bolinhas_nao_sorteadas = qtd_numeros
        self.__ultimo_numero_sorteado = None
        self.__todos_numeros_sorteados = False

    @property
    def qtd_numeros(self):
        return self.__qtd_numeros

    @property
    def numeros(self):
        return self.__numeros

    @property
    def bolinhas_sorteadas(self):
        return self.__bolinhas_sorteadas

    @property
    def qtd_bolinhas_sorteadas(self):
        return self.__qtd_bolinhas_sorteadas

    @property
    def qtd_bolinhas_nao_sorteadas(self):
        return self.__qtd_bolinhas_nao_sorteadas

    @property
    def ultimo_numero_sorteado(self):
        return self.__ultimo_numero_sorteado

    @property
    def todos_numeros_sorteados(self):
        return self.__todos_numeros_sorteados

    def sortear_numero(self):
        if self.__todos_numeros_sorteados == True:
            return
    
        numero_sorteado = random.choice(self.__numeros)

        self.__ultimo_numero_sorteado = numero_sorteado
        self.__numeros.remove(numero_sorteado)
        self.__bolinhas_sorteadas.append(numero_sorteado)
        self.__qtd_bolinhas_sorteadas += 1
        self.__qtd_bolinhas_nao_sorteadas -= 1

        if not self.__numeros:
            self.__todos_numeros_sorteados = True