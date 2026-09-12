# importando o método construtor da classe 'Data'
from Data import Data

a = Data(False, 4, 11, 2021)
b = Data(False, 11, 9, 2001)
c = Data()

print("Joaquim nasceu em", a.toString(True))
print("O atentado nas torres gêmeas aconteceu em", b.toString(True))
print("Hoje é", c.toString(False))