"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

nome = 'Joao Gabriel'
print(nome)
print(type(nome))

nome = "Joao´s Gabriel"
print(nome)
print(type(nome))

nome = 'Joao \nGabriel'
print(nome)
print(type(nome))

nome = "Joao \"Gabriel"
print(nome)
print(type(nome))

nome = 'Joao Gabriel'
print(nome.upper())

nome = 'Joao Gabriel'
print(nome.lower())

nome = 'Joao Gabriel'
print(nome.split()) #transforma em uma lista de strings

print(nome[0:4]) # Slice de string

print(nome[5:15]) # Slice de string

# [ 0,          1]
# ['Joao', 'Gabriel']
print(nome.split()[0])

print(nome.split()[1])
"""
# Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11 ]
# ['J', 'o', 'ã', 'o', ' ', 'G', 'a', 'b', 'r', 'i', 'e', 'l']

nome = 'Joao Gabriel'

"""
[::-1] -> Comece dp primeiro elemento, vá até o último e inverta
"""
print(nome[::-1])  #Inversão da String Phythônico

print(nome.replace('e', 'i'))

print(nome(type))

texto = 'socorram me subino onibus em marrocos'
print(texto)

print(texto[::-1])



