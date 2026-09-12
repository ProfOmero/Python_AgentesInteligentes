# importando o método construtor da classe 'Ponto'
from Ponto import Ponto
import sys
sys.path.insert(1, 'C:\Python_AgentesInteligentes\Fontes\Python')
from Geral import cls

cls()

n = int(input("Quantos ponto serão informados? "))

pontos = []
for i in range(n):
    print()
    print(f"{i+1}o. ponto: ")

    x = int(input("Coordenada 'x': "))
    y = int(input("Coordenada 'y': "))

    # instanciando o objeto 'p' a partir da classe 'Ponto'
    p = Ponto(x, y)
    # adiciona o objeto 'p' a lista de objetos 'pontos'
    pontos.append(p)

print()
for i in range(n):
    print(f"{i+1}o. ponto: {pontos[i]}")
