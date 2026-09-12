from datetime import datetime

class Data:
    def __init__(self, dataDeHoje=True, dia=0, mes=0, ano=0):
        if (dataDeHoje):
            # data do sistema operacional
            hoje = datetime.now()
            self.dia = hoje.day
            self.mes = hoje.month
            self.ano = hoje.year
        else:
            self.dia = dia
            self.mes = mes
            self.ano = ano

    # métodos de acesso (getters e setters)
    def getDia(self):
        return(self.dia)

    def setDia(self, dia):
        self.dia = dia

    def getMes(self):
        return(self.mes)

    def setMes(self, mes):
        self.mes = mes

    def getAno(self):
        return(self.ano)

    def setAno(self, ano):
        self.ano = ano

    def calcularIdade(self):
        hoje = datetime.now() # data de hoje

        idade = hoje.year - self.ano
        if ((hoje.month < self.mes) or ((hoje.month == self.mes) and (hoje.day < self.dia))):
            idade = idade - 1

        return(idade)

    def nomeDoMes(self):
        meses = ["", "jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]

        return(meses[self.mes])

    def toString(self, mostrarIdade):
        if (mostrarIdade):
            result = f"{self.dia:02d}/{self.nomeDoMes()}/{self.ano} ({self.calcularIdade()} anos)"
        else:
            result = f"{self.dia:02d}/{self.nomeDoMes()}/{self.ano}" 

        return result    