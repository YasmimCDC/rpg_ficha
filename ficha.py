#Classe para armazenar informaçoes basicas do personagem criado pelo jogador

class Ficha:
    def __init__(self, classe, dinheiro = 400):
        self.__dinheiro = dinheiro
        self.__classe = classe

    def getDinheiro(self):
        return self.__dinheiro

    def setDinheiro(self, dinheiro):
        self.__dinheiro = dinheiro

    def getClasse(self):
        return self.__classe