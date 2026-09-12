def calcular_IMC(pc, alt):
    vlrIMC = pc / (alt ** 2)
    return vlrIMC

def interpretar_IMC(vlrIMC):
    # sistema baseado em regras (5 regras)
    if (vlrIMC < 18.5):
        return "Magreza"
    elif (vlrIMC < 25.0):
        return "Peso normal"
    elif (vlrIMC < 30.0):
        return "Sobrepeso"
    elif (vlrIMC < 40.0):
        return "Obesidade"
    else:
        return "Obesidade grave"

def toString(paciente, pc, alt):
    vlrIMC = calcular_IMC(pc, alt)
    interpretacao = interpretar_IMC(vlrIMC)

    result = f"Paciente............: {paciente}\n"
    result += f"Peso corporal.......: {pc:.3f} kg\n"
    result += f"Altura..............: {alt:.2f} metros\n"
    result += f"IMC.................: {vlrIMC:.2f}\n"
    result += f"Interpretação do IMC: {interpretacao}\n"

    return(result)