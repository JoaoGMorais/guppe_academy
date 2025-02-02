"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais;
  -Variáveis globais sçao reconhecidas, ou seja, seu escopo compreende, todo o o programa.

2 - Variáveis locais;
   -Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
   está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuímos o valor á mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;
"""
numero = 42 # Exemplo de variavel global
print(numero)
print(type(numero))

nao_existo = 'oi'
print(nao_existo)

numero = 42
# novo = 0

if numero > 10:
    novo = numero + 10 # A variavel 'novo' está declarada localmente dentro do bloco do if. Portanto, é local
    print(novo)

print(novo)















