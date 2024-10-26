"""
PEP8 - Python Enhancement Proposal

São Propostas de melhorias para a linguagem Python

Zen of Python

import this

A ideia da PEP8  é que possamos escrever códigos python de forma pythônica.

[1] - Utilize camel case para nomes de classes;
class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minusculo , separados por underline para funções ou variáveis;
def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

[3] - Utilize 4 espaços para identação!!! [NÃO USE TAB]
if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
-Separar funções e definições de classe com duas linhas em branco;
-Métodos dentro de uma classe devem ser separados com uma única linha em branco;

class Classe:
    pass

class Outra:
    pass

[5] - Imports
-Imports devem ser sempre feitos em linhas separadas

#Import Errado

import sys, os

#Import Correto

import  sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType,
)

# Imports devem ser colocados no top do arquivo, logo depois de quaisquer comentários ou docstrings e
# Antes de constantes ou variáveis globais.
# Sempre no topo do programa.

[6] - Espaços em expressões e instruções
# Não faça:

funcao( algo[ 1 ], { outro: 2 } )

# Faça:
funcao(algo[1], {outro: 2})

[7] - Termine sempre uma instrução com uma nova linha
"""
import this



class Calculadora:
    pass


class CalculadoraCientifica:
    pass


def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5


if 'a' in 'banana':
    print('tem')


class Classe:
    pass

class Outra:
    pass


#Import Errado

import sys, os

#Import Correto

import  sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType,
)

# Imports devem ser colocados no top do arquivo, logo depois de quaisquer comentários ou docstrings e
# Antes de constantes ou variáveis globais.
# Sempre no topo do programa.


# Não faça:

funcao( algo[ 1 ], { outro: 2 } )

# Faça:
funcao(algo[1], {outro: 2})
