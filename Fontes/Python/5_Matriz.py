def matriz_I(n):
    i = 0
    while (i < n):
        j = 0
        while (j < n):
            print(f"{i}{j}", end=" ")
            j += 1
        print()
        i += 1

def matriz_II(n):
    for i in range(n): # equivale a um for each
        for j in range(n):
            print(f"{i}{j}", end=" ")
        print()

# módulo principal (main)
n = int(input("Digite o tamanho da matriz: "))

print()
matriz_I(n)
print()
matriz_II(n)