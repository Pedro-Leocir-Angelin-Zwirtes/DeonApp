# DeonApp
Projeto criado em Python para a mecânica deon no auxilio de passar as ordens para o sistema

# Como funciona
A interface é simples, basta apenas digitar o numero de ordens passados pelo funcionario <br>
Ex:
  - 800 1200

O programa vai retornar 4 h : 0 min.
Que corresponde ao diferença de tempo das 8:00 até o 12:00

# Problemas na instalação do projeto
Em algumas versões do windows encontrei problemas com o pyinstaller no modo convencional de instalar então pode se usar o seguinte comando: <br><br>
pyinstaller -F main.py --collect-all customtkinter -w -i logo.ico
