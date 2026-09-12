import Geral
from random import randint
from Vetor import saida
from Meu_Math import divisores, ehPrimo

Geral.cls()

for i in range(1, 11):
    nro = randint(1, 50)

    x = divisores(nro)
    print(saida(f"Divisores de {nro}", x), end=" ")
    if (ehPrimo(nro)):
        print("<<< número primo >>>")
    else:
        print()
        
    Geral.delay(1)
    Geral.linha(tipo="-", tam=50)

print()
print("<<< FIM DO PROGRAMA >>>")
Geral.parada()