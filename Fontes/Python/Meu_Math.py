def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def divInt(a, b):
    if (b == 0):
        return 0
    return a // b

def divReal(a, b):
    if (b == 0):
        return 0
    return a / b

def toString(a, b):
    result = f"{a} + {b} = {soma(a, b)}\n"
    result += f"{a} - {b} = {sub(a, b)}\n"
    result += f"{a} * {b} = {mult(a, b)}\n"
    result += f"{a} // {b} = {divInt(a, b)} divisão inteira\n"
    result += f"{a} / {b} = {divReal(a, b):.2f} divisão real\n"

    return result

def divisores(n):
    result = []
    for i in range(1, n + 1):
        if (n % i == 0):
            result.append(i)

    return result

def ehPrimo(n):
    return(len(divisores(n)) == 2)