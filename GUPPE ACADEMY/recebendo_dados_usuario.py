"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo string

Em Python , string é tudo que estiver entre:
-Aspas simples;
-Aspas duplas;
-Aspas simples triplas;
-Aspas duplas triplas;

Ex:
-Aspas simples -> 'Joao Gabriel'
-Aspas duplas -> "Joao Gabriel"
-Aspas simples triplas -> '''Joao Gabriel'''
"""
# - Aspas duplas triplas -> """Joao Gabriel"""

# Entrada de dados
#print("Qual seu nome? ")
#nome = input() #Input -> Entrada

nome = input('Qual seu nome? ')

# Exemplo de print 'antigo' 2.x
#print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
#print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}')

#print("Qual a sua idade? ")
#idade = input()

idade = int(input('Qual sua idade? '))


# Processamento


# Saída de dados
# Exemplo de print 'antigo' 2.x
#print('A %s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
#print('A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'A {nome} tem {idade} anos')

"""
# int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""

print(f'A {nome} nasceu em {2024 - idade}')
