"""
2. Faça um programa que peça para o usuário digitar três valores inteiro e imprima a soma deles.
"""
from escopo_de_variaveis import numero

numero1: int = int(input("Infrome um numero inteiro: "))
numero2: int = int(input("Infrome um numero inteiro: "))
numero3: int = int(input("Infrome um numero inteiro: "))

soma: int = numero1 + numero2 + numero3

print(f"A soma dos numeros {numero1} com {numero2} e {numero3} é {soma}")