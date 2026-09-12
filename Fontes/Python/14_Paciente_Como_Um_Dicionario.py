from Calculadora_IMC import toString
from Geral import cls, delay, confirmou

meu_Paciente = {
    "paciente": "",
    "pc": 0.0,
    "alt": 0.0    
}

arquivo = open("pacientes.txt", "a")

while True:
    cls()
    print(f"<<< CADASTRO DE PACIENTES >>>")
    print()

    meu_Paciente["paciente"] = input("Nome do paciente (FIM para encerrar):\n")
    if (meu_Paciente["paciente"].upper() == "FIM"):
        break

    print()
    meu_Paciente["pc"] = float(input("Peso do paciente (kg)  = "))
    meu_Paciente["alt"] = float(input("Altura do paciente (m) = "))
    print()
    print()
    print(toString(meu_Paciente["paciente"], meu_Paciente["pc"], meu_Paciente["alt"]))
    print()
    if (confirmou("Confirma o cadastro do paciente (s/n)? ")):
        arquivo.write(f"{meu_Paciente['paciente']};{meu_Paciente['pc']};{meu_Paciente['alt']}\n")   
        print("<<< PACIENTE CADASTRADO COM SUCESSO >>>")
        delay(2)

cls()
arquivo.close()
print("<<< FIM DO CADASTRO DE PACIENTES >>>")
