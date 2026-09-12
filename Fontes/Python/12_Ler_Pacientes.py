import Calculadora_IMC
import Geral

Geral.cls()

arquivo = open("Pacientes.txt", "r")

linhasDoArquivo = arquivo.readlines()

for linha in linhasDoArquivo:
    partes = linha.split(";")

    paciente = partes[0]
    pc = float(partes[1])
    alt = float(partes[2])

    print(Calculadora_IMC.toString(paciente, pc, alt))

arquivo.close()