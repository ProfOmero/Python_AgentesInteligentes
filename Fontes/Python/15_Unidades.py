from random import randint
from Geral import cls

def descricao_unidade(i):
    unidades = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
    return unidades[i]

# módulo principal (main)
cls()

n = int(input("Quantas unidades serão geradas ? "))

print()
for i in range(n):
    unidade = randint(0, 9)
    print(f"Unidade gerada: {unidade} - {descricao_unidade(unidade)}")

