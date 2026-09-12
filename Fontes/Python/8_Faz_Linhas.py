def linha(tipo="*", tam=10):
    result = ""
    for i in range(tam):
        result += tipo

    return(result)

# módulo principal (main)
print(linha())
print(linha(tipo="+"))
print(linha(tipo="-", tam=20))
print(linha(tam=30))
print(linha(tipo="ABC", tam=5))