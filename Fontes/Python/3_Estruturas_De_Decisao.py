def sinal_I(n):
    if (n < 0):
        return "<<< NEGATIVO >>>"

    if (n == 0):
        return "<<< NEUTRO >>>"

    if (n > 0):
        return "<<< POSITIVO >>>"

def sinal_II(n):
    if (n < 0):
        return "<<< NEGATIVO >>>"
    else:
        if (n == 0):
            return "<<< NEUTRO >>>"
        else:
            return "<<< POSITIVO >>>"

def sinal_III(n):
    if (n < 0):
        return "<<< NEGATIVO >>>"
    elif (n == 0):
        return "<<< NEUTRO >>>"
    else:
        return "<<< POSITIVO >>>"

# módulo principal (main)
tam = int(input("Quantos números deseja verificar? "))

for i in range(tam):
    print()
    n = int(input(f"Digite o {i + 1}º número: "))

    print(sinal_I(n))
    print(sinal_II(n))
    print(sinal_III(n))  