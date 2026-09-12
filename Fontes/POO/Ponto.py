class Ponto:
    # método construtor (faz a instanciação do objeto da classe)
    def __init__(self, x, y):
        # declarando os atributos "x" e "y"
        self.x = x
        self.y = y

    # métodos de acesso (getters e setters)
    def getX(self): # método equivale a um módulo python
        return(self.x)

    def setX(self, x):
        self.x = x

    def getY(self):
        return(self.y)

    def setY(self, y):
        self.y = y

    def posicao(self):
        if ((self.x > 0) and (self.y > 0)):
            return("Q1")
        elif ((self.x < 0) and (self.y > 0)):
            return("Q2")
        elif ((self.x < 0) and (self.y < 0)):
            return("Q3")
        elif ((self.x > 0) and (self.y < 0)):
            return("Q4") 
        elif ((self.x != 0) and (self.y == 0)):
            return("Eixo X")               
        elif ((self.x == 0) and (self.y != 0)):
            return("Eixo Y")
        else:
            return("Origem")        

    # equivale ao método 'toString' de outras linguagens
    def __str__(self):
        return f"(x: {self.x}, y: {self.y}) = {self.posicao()}"