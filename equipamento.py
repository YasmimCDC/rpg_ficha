#Classe que armazena os itens dopersonagem

from Projeto.classe import *
from Projeto.ficha import *

class Equipamento:

    def __init__(self,ficha):
        self.__ficha = ficha
        self.__compra = list()

    def getItens(self):
        return self.__compra

    def setItens(self, itens):
        self.__compra = itens

    def adicionarItem(self, item):
        self.__compra.append(item)

    #Metodo que adiciona objeto e desconta o dinheiro
    def compra(self, item):
        if self.__ficha.getDinheiro() >= item.getPreco() and self.__ficha.getClasse().getForca() >= item.getFn():
            self.__ficha.setDinheiro(self.__ficha.getDinheiro() - item.getPreco())
            self.__compra.append(item)

    #metodo de retirada de itens do personagem
    def removerItemDeCompra(self, item):
        for x in self.__compra:
            if x.getNome() == item :
                self.__compra.remove(x)
                self.__ficha.setDinheiro(self.__ficha.getDinheiro() + x.getPreco())

    def mostrarCompras(self):
        for x in self.__compra:
            print(x.getNome())