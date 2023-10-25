import customtkinter
from datetime import datetime

#Sistemas para calcular varias horas
def calcular_diferenca_horas(inicio, termino):
    formato = '%H%M'
    hora_inicio = datetime.strptime(inicio, formato)
    hora_termino = datetime.strptime(termino, formato)
    diferenca = hora_termino - hora_inicio
    return diferenca

#criando as funções de cada botão
def calcular_valor(valor, resultado):
    try:
        horas_text = valor
        horas_linhas = horas_text.strip().split('\n')
        soma_total_horas = 0

        for linha in horas_linhas:
            inicio, termino = linha.split()
            diferenca = calcular_diferenca_horas(inicio, termino)
            soma_total_horas += diferenca.total_seconds() / 3600

        horas_inteiras = int(soma_total_horas)
        minutos_fracionados = round(((soma_total_horas - horas_inteiras) * 60),2)

        resultado_text = f"{horas_inteiras} h : {int(minutos_fracionados)} min"
        resultado.configure(text=resultado_text)
    except ValueError:
        resultado.configure(text="Valor inválido!")

#Sistemas para calcular varios materiais
def calcular_material(valor2, resultado2):
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
