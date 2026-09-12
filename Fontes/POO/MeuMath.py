class MeuMath:
    # método construtor (faz a instanciação do objeto da classe)
    def __init__(self, a, b):
        # declarando os atributos "a" e "b"
        self.a = a
        self.b = b

    # métodos de acesso (getters e setters)
    def getA(self): # método equivale a um módulo python
        return(self.a)

    def setA(self, a):
        self.a = a

    def getB(self):
        return(self.b)

    def setB(self, b):
        self.b = b

    def soma(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def divInt(self):
        if (self.b == 0):
            return 0
        return self.a // self.b

    def divReal(self):
        if (self.b == 0):
            return 0
        return self.a / self.b      

    # equivale ao método 'toString' de outras linguagens
    def __str__(self):
        result = f"{self.a} + {self.b} = {self.soma()}\n"
        result += f"{self.a} - {self.b} = {self.sub()}\n"
        result += f"{self.a} * {self.b} = {self.mult()}\n"
        result += f"{self.a} // {self.b} = {self.divInt()} divisão inteira\n"
        result += f"{self.a} / {self.b} = {self.divReal():.2f} divisão real\n"

        return result
