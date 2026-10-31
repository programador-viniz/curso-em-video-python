"""
Exercício 001
Objetivo: Criar um programa que exiba a mensagem "Olá, Mundo!" na tela.
"""

#Importando a biblioteca colorama para colorir o texto
from colorama import Fore, Style, init

init(autoreset=True) #Resetar as cores após cada impressão

print(Fore.GREEN + Style.BRIGHT + "\nOlá, Mundo!\n")
