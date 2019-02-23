#Classe mae que contem todas as caracteristicas em comum das Classes do jogo
class Classe:

    __forca = 0
    __agilidade = 0
    __inteligencia = 0
    __espirito = 0
    __vontade = 0
    __nome_da_classe = ""
    __raca = ""

    def __init__(self, nome_da_classe, raca, forca = 3, agilidade = 3, inteligencia = 3, espirito = 3, vontade = 3):
        self.__nome_da_classe = nome_da_classe
        self.__raca = raca
        self.__forca = forca
        self.__agilidade = agilidade
        self.__inteligencia = inteligencia
        self.__espirito = espirito
        self.__vontade = vontade

    def getNomeDaClasse(self):
        return self.__nome_da_classe

    def setNomeDaClasse(self, nome):
        self.__nome_da_classe = nome

    def getRaca(self):
        return self.__raca

    def setRaca(self, raca):
        self.__raca = raca

    def getForca(self):
        return self.__forca

    def setForca(self, forca):
        self.__forca = forca

    def getAgilidade(self):
        return self.__agilidade

    def setAgilidade(self, agilidade):
        self.__agilidade = agilidade

    def getInteligencia(self):
        return self.__inteligencia

    def setInteligencia(self, inteligencia):
        self.__inteligencia = inteligencia

    def getEspirito(self):
        return self.__espirito

    def setEspirito(self, espirito):
        self.__espirito = espirito

    def getVontade(self):
        return self.__vontade

    def setVontade(self, vontade):
        self.__vontade = vontade

    #funçao de acrescimo de artibutos
    def incrementoRaca(self):
        if self.getRaca() == "elfo":
            self.__inteligencia += 1
            self.__espirito += 1

        if self.getRaca() == "humano":
            self.__forca += 1
            self.__vontade += 1

        if self.getRaca() == "anão":
            self.__vontade += 1
            self.__espirito += 1

        if self.getRaca() == "gnomo":
            self.__inteligencia += 1
            self.__agilidade += 1

        if self.getRaca() == "orc":
            self.__agilidade += 1
            self.__forca += 1

    #formataçao do "print" para os atributos do jogador
    def imprimirAtributos(self):
        self.incrementoRaca()
        print("Atributos: ")
        print("- Força = ", self.getForca(), "\n"
              "- Agilidade = ", self.getAgilidade(), "\n"
              "- Inteligência = ", self.getInteligencia(), "\n"
              "- Espírito = ", self.getEspirito(), "\n"
              "- Vontade = ", self.getVontade())
