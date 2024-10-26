"""
Exercicio 3
Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.
"""

valor1: int = int(input('Informe o primeiro inteiro: '))
valor2: int = int(input('Informe o segundo inteiro: '))
valor3: int = int(input('Informe o terceiro inteiro: '))

soma: int = (valor1 * valor1) + (valor2 * valor2) + (valor3 * valor3)

print(f"A soma dos quadrados dos valores {valor1} com {valor2} e {valor3} é {soma}")