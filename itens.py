#Classe com as caracteristicas que um item do jogo possui
class Item:

    def __init__(self,nome, preco = 0, dano = 0, defesa = 0, fn = 0, quantidade = 0, portadores = []):
        self.__nome = nome
        self.__preco = preco
        self.__dano = dano
        self.__defesa = defesa
        self.__fn = fn
        self.__quantidade = quantidade
        self.__portadores = portadores

    def setPortadores(self, portadores):
        self.__portadores = portadores

    def getPortadores(self):
        return self.__portadores

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setPreco(self, preco):
        self.__preco = preco

    def getPreco(self):
        return self.__preco

    def setDano(self, dano):
        self.__dano = dano

    def getDano(self):
        return self.__dano

    def setDefesa(self,defesa):
        self.__defesa = defesa

    def getDefesa(self):
        return self.__defesa

    def setFn(self,fn):
        self.__fn = fn

    def getFn(self):
        return self.__fn

    def setQuantidade(self, quantidade):
            self.__quantidade = quantidade

    def getQuantidade(self):
        return self.__quantidade
