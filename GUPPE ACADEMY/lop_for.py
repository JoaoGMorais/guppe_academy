"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

C ou Java

for(int i = 0; i < 10; i++){
    //execução do loop
}

Python

for item in interavel:
    //execução do loop


Utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis.
Exemplos:
- String
    nome = 'Joao Gabriel'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)

nome = 'Joao Gabriel'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

# Exemplo de for 1 (iterando sobre uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando sobre umas lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (iterando sobre um range)

range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não
for numero in range(1, 10):
    print(numero)

nome = 'Joao Gabriel'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

Enumerate:

((0, 'J'), (1, 'O'), (2, 'a'), (3, 'o'), (4, ' '), (5, 'G'), (6, 'a'), .................)

for i, letra in enumerate(nome):
    print(nome[i])

for i, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)
OBS: Quando não precisamos de um valor, podemos descarta-los utilizando um underline (_)

for valor in enumerate(nome):
    print(valor)

qnt = int(input('Quantas Vezes esse loop deve rodar?'))
soma = 0

for n in range(1, qnt+1):
    num = int(input(f'Imprimindo {n}/{qnt} valor: '))
    soma = soma + num
    print(f'A soma é {soma}')

nome = 'Joao Gabriel'
for letra in nome:
    print(letra, end='')

Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""
# Original: U+1F60D
# Modificado: U0001F60D
for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)














