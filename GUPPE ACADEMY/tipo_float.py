"""
Tipo Float

Tipo real, decimal

Casas decimais
OBS: O separador de casas deciamis na programção é o ponto e não a virgula.
"""

# Errado do ponto de vista do float, mas gera uma tupla
valor = 1,44

# Correto do ponto de vista do float
valor = 1.44
print(valor)
print(type(valor))

# É Possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Pode converter um float para int
"""
OBS: Ao converter valores float para int, nos prdemos precisão.
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j
