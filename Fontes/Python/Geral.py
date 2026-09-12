from os import system
from time import sleep

def cls():
    system("cls")

def delay(tmp): # tmp = tempo em segundos
    sleep(tmp)

def parada():
    print()
    input("Pressione <ENTER> para continuar...")

def confirmou(rotulo):
    op = input(rotulo)
    if ((op == "s") or (op == "S")):
        return True
    return False

def linha(tipo="*", tam=10):
    result = ""
    for i in range(tam):
        result += tipo

    return(result)