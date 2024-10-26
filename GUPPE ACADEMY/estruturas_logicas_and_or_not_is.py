"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not
Operadores binários:
    -and,or, is

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not' o valor do boleano é invertido, ou seja se for True, vira False, se for False vira True
Para o 'is' o valor é comaprado com um segundo
"""
ativo = True
logado = False

if ativo:
    print('Bem-vindo usuario!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

print(ativo is False)


