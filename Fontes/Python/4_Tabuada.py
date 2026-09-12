def tabuada_I(n):
    i = 1 # variável de controle do laço
    while (i <= 10):
        print(f"{n} x {i} = {n * i}")
        i += 1 # passo do laço

def tabuada_II(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


# módulo principal (main)
while (True):
    n = int(input("De 0 até 10, -1 para sair. Tabuada do "))
    if (n == -1):
        break

    if (n < 0 or n > 10):
        print("Número inválido, digite novamente.\n")
        continue

    print()
    print("Tabuada usando while:")
    tabuada_I(n)

    print()
    print("Tabuada usando for:")
    tabuada_II(n)
    print()
