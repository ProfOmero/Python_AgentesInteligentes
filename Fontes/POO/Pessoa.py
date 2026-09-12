from Data import Data

class Pessoa:
    def __init__(self, nome, sexo, dtNasc):
        self.nome = nome
        self.sexo = sexo
        # relacionamento de associação feito através
        # do atributo 'dtNasc' e a Classe 'Data'
        self.dtNasc = dtNasc # data de nascimento

    def getNome(self):
        return(self.nome)

    def setNome(self, nome):
        self.nome = nome

    def getSexo(self):
        return(self.sexo)

    def setSexo(self, sexo):
        self.sexo = sexo

    def getDtNasc(self):
        return(self.dtNasc)

    def setDtNasc(self, dtNasc):
        self.dtNasc = dtNasc

    def __str__(self):
        result =  f"Nome......: {self.nome}\n"
        result += f"Sexo......: {self.sexo}\n"
        result += f"Nascimento: {self.dtNasc.toString(True)}\n"

        return result     
        