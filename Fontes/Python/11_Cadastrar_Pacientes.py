from Geral import cls, delay, parada, confirmou

arquivo = open("Pacientes.txt", "a")

cls()
n = int(input("Número de pacientes a cadastrar = "))

i = 1
while (i <= n):
    cls()
    print(f"<<< CADASTRO DE PACIENTES ({i}/{n}) >>>")
    print()

    nome = input("Nome do paciente       = ")
    peso = float(input("Peso do paciente (kg)  = "))
    altura = float(input("Altura do paciente (m) = "))
    print()

    if (confirmou("Confirma o cadastro do paciente (s/n)? ")):
        arquivo.write(f"{nome};{peso};{altura}\n")
        i += 1 # próximo paciente

        print("<<< PACIENTE CADASTRADO COM SUCESSO >>>")
        delay(2)

arquivo.close()
print()
print("<<< CADASTRO DE PACIENTES FINALIZADO >>>")
parada()