from math import sqrt

def dobro(n):
    return n * 2

def triplo(n):
    return n * 3

def quadrado(n):
    return n ** 2

def cubo(n):
    return n ** 3

def raizQuadrada(n):
    return sqrt(n)

def toString(n):
    result = f"Sendo n = {n}, tem-se:\n"
    result += f"  Dobro: {dobro(n)}\n"
    result += f"  Triplo: {triplo(n)}\n"
    result += f"  Quadrado: {quadrado(n)}\n"
    result += f"  Cubo: {cubo(n)}\n"
    result += f"  Raiz Quadrada: {raizQuadrada(n):.2f}\n"
    return result

# módulo principal
n = int(input("N: "))

print()
print(toString(n))