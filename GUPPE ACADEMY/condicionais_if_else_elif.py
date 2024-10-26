"""
Estruturas condicionais
if, else, elif
"""

idade = 26

"""
# Estrutura condicional if, else, em C:

if(idade < 18){
    printf("menor de idade");
}else{
  printf("maior de idade");
}
"""
"""
# Estrutura condicional if, else em Java:

if(idade < 18){
    System.out.println("menor de idade");
}else{
  System.out.println("maior de idade");
}
"""

if idade < 18:
    print('menor de idade')
elif idade == 18:
    print('tem 18 anos')
elif idade == 26:
    print('tem 26 anos')
else:
    print('maior de idade')
