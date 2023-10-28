# DeonApp
Projeto criado em Python para a mecânica deon no auxilio de passar as ordens para o sistema

# Como funciona
A interface é simples temos 2 campos para entrada de valores e 2 checkbox acima de cada campo, basta apenas escolher uma das opções e preencher o campo para calcular.

# Calcular horas
Após selecionar a opção calcular horas o campo de entrada deve ser preenchido da seguinte maneira
<br><br>
Ex 1: <br><br>
    800 1200 <br>
    300 1457 <br>

retorno vai ser 5 h 57 min <br><br>

Ex 2: <br><br>
    800 1200 <br>

retorno vai ser 4 h 0 min <br><br>

# Somar horas
Após selecionar a opção somar horas o campo de entrada deve ser preenchido da seguinte maneira
<br><br>
Ex 1: <br><br>
    157 340 <br>

retorno vai ser 5 h 37 min <br><br>

# Calcular Materiais
Após selecionar a opção calcular materiais o campo de entrada deve ser preenchido da seguinte maneira
<br><br>
Ex 1: <br><br>
    200 3 <br>
    400 5 <br>
    
retorno vai ser 2600 mm(s) <br><br>

Ex 2: <br><br>
    200 3 <br>
    
retorno vai ser 600 mm(s) <br><br>

# Calcular chapas
Após selecionar a opção calcular chapas o campo de entrada deve ser preenchido da seguinte maneira
<br><br>
Ex 1: <br><br>
    200 300 (tipo da chapa) 3/16 <br>
    
retorno vai ser 2.28 Kg(s) mm(s) <br>
Vale informar que as medidas das chapas os funcionários da mecânica já conhecem.

# Instalação

Primeiro instale o Python em sua máquina e logo após use o comando. <br><br>

$ pip install -r requirements.txt <br><br>

Feito isso você pode instalar o programa como um executável em sua máquina com o comando <br><br>

$ pyinstaller -F main.py --collect-all customtkinter -w -i logo.ico

