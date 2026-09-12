from Pessoa import Pessoa

import sys
sys.path.insert(1, "C:\Python_AgentesInteligentes\Fontes\Python")
from Calculadora_IMC import calcular_IMC, interpretar_IMC

class PacienteIMC(Pessoa):
    # método construtor da classe "PacienteIMC"
    def __init__(self, nome, sexo, dtNasc, pc, alt):
        super().__init__(nome, sexo, dtNasc)
        # atributos particulares da classe "PacienteIMC"
        self.pc = pc
        self.alt = alt

    def getPC(self):
        return(self.pc)

    def setPC(self, pc):
        self.pc = pc

    def getAlt(self):
        return(self.alt)

    def setAlt(self, alt):
        self.alt = alt

    def __str__(self):
        vlr_IMC = calcular_IMC(self.pc, self.alt)
        interpretacao = interpretar_IMC(vlr_IMC)

        result = super().__str__()
        result += f"Peso......: {self.pc:.3f} kgs\n"
        result += f"Altura....: {self.alt} metros\n"
        result += f"IMC.......: {vlr_IMC:.2f} <<< {interpretacao} >>>\n"

        return result