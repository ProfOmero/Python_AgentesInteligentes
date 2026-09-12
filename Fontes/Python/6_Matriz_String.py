def matriz_String(s):
    n = len(s)
    for i in range(n):
        for j in range(i+1):
            print(s[j], end=" ")
        print()

# módulo principal (main)
s = input("Digite uma string: ")

print()
matriz_String(s)