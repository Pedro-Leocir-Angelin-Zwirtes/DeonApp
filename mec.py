import customtkinter
from datetime import datetime

class Mec:
    """docstring for Mec"""
    def __init__(self):
        self.STATUS_BOTAO = 0
        

    #Sistemas para calcular varias horas
    def calcular_diferenca_horas(self, inicio, termino):
        formato = '%H%M'
        hora_inicio = datetime.strptime(inicio, formato)
        hora_termino = datetime.strptime(termino, formato)
        diferenca = hora_termino - hora_inicio
        return diferenca

    #criando as funções de cada botão
    def calcular_valor(self, valor, resultado):
        try:
            horas_text = valor
            horas_linhas = horas_text.strip().split('\n')
            soma_total_horas = 0

            for linha in horas_linhas:
                inicio, termino = linha.split()
                diferenca = self.calcular_diferenca_horas(inicio, termino)
                soma_total_horas += diferenca.total_seconds() / 3600

            horas_inteiras = int(soma_total_horas)
            minutos_fracionados = round(((soma_total_horas - horas_inteiras) * 60),2)

            resultado_text = f"{horas_inteiras} h : {int(minutos_fracionados)} min"
            resultado.configure(text=resultado_text)
        except ValueError:
            resultado.configure(text="Valor inválido!")

    #calcular hora somadas
    def somar_horas(self, valor, resultado):
        try:
            
            horas_text = valor
            horas_linhas = horas_text.strip().split('\n')
            soma_total_horas = 0

            for linha in horas_linhas:
                hora1, hora2 = linha.split()

                horas1, minutos1 = divmod(int(hora1), 100)
                horas2, minutos2 = divmod(int(hora2), 100)

                total_horas = horas1 + horas2
                total_minutos = minutos1 + minutos2

                if total_minutos >= 60:
                    total_horas += 1
                    total_minutos -= 60

                resultados = f"{total_horas}"
                if total_minutos > 0:
                    resultados += f"{total_minutos}"

                if total_horas > 0:

                    tam = len(str(total_horas))

                    resultado_text = f"{resultados[:tam]} h : {resultados[tam:]}"
                    resultado.configure(text=resultado_text)

                else:
                    resultado_text = f"{resultados[1:]} min"
                    resultado.configure(text=resultado_text)

        except ValueError:
            resultado.configure(text="Valor inválido!")

    #Sistemas para calcular varios materiais
    def calcular_chapas(self, valor2, resultado2):
        try:
            matirial = valor2
            material_linhas = matirial.strip().split('\n')
            peso_chapas = 0

            for linha in material_linhas:
                medida1, medida2, chapa = linha.split()
                if chapa == '3/16':
                    peso_chapas += ((int(medida1)/10 * int(medida2)/10) * 38) / 10000

            resultado_text = f"{round(peso_chapas, 2)} Kg(s)"
            resultado2.configure(text=resultado_text)
        except ValueError:
            resultado2.configure(text="Valor inválido!")

    def calcular_material(self, valor2, resultado2):
        try:
            matirial = valor2
            material_linhas = matirial.strip().split('\n')
            soma_material = 0

            for linha in material_linhas:
                medida, quantidade = linha.split()
                soma_material += int(medida) * int(quantidade) 

            resultado_text = f"{soma_material} mm(s)"
            resultado2.configure(text=resultado_text)
        except ValueError:
            resultado2.configure(text="Valor inválido!")

    #Logica dos checkbox na parte de horas
    def verificar_status(self, valor_check, valor_check2, checkbox1, checkbox2):
        status_valor = valor_check
        status_valor2 = valor_check2

        if status_valor == 'off' and status_valor2 == 'off':
            checkbox1.configure(state='normal')
            checkbox2.configure(state='normal')

            self.STATUS_BOTAO = 1

        else:
            if status_valor == 'on' and status_valor2 == 'off':
                checkbox1.configure(state='normal')
                checkbox2.configure(state='disabled')

                self.STATUS_BOTAO = 2

            elif status_valor2 == 'on' and status_valor == 'off':
                checkbox1.configure(state='disabled')
                checkbox2.configure(state='normal')

                self.STATUS_BOTAO = 3
