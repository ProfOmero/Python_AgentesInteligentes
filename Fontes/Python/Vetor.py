def entrada(id, tam):
    x = []
    for i in range(tam):
        x.append(int(input(f"{i+1}o. valor, {id}[{i}] = ")))

    print()
    return x

def saida(id, x):
    tam = len(x)

    result = f"{id} = ["
    for i in range(tam):
        result += f"{x[i]}"
        if (i < tam - 1):
            result += ", "
    result += "]"

    return result

def somar(x):
    return(sum(x))

def media(x):
    return(sum(x) / len(x))

def toString(id, x):
    result = saida(id, x) + "\n"
    result += f"Soma dos valores  = {somar(x)}\n"
    result += f"Média dos valores = {media(x):.2f}\n"

    return(result)