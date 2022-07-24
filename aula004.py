"""
-------------------------------------------------------------------
primeiros scripts
-PRIMEIROS COMANDOS EM PYHTON
-- mostrando coisas para o usuario, e perguntando coisas ao usuario
--------------------------------------------------------------------
dados, se forem msg, tem delimitadores especiais

no pthon, são aspas simples ou duplas (' '," ")
-msg-
-'msg'-
-('msg')-
-print('msg')-
todos comandos são funçoes, toda funcao tem ()
ex: print()
nem tudo em python é msg, numeros sem aspas por exemplo
- Mensagens sao primordialmente para mostrar algo na tela
print('Ola, Mundo!!')
- Numeros sao primordialmente para fazer calculo
print(7 + 4)
juntando mensagens - usa-se '+' ou ','
print('7' + '4')
"""
"""
#pratica
print('Ola Mundo')
#ERROR - print(Ola, Mundo)
print(7 + 4)
print('7' + '4')
#ERROR - print('Ola' + 5)
print('Ola', 5)
"""
"""
Usando variaveis - usar sempre letras minusculas
toda variavel é um objeto 
toda variavel recebe algo(msg ou valores), usando '='
ex: nome     =       'Kawa Max'
    /        |              \
variavel   recebe           texto/mensagem
"""
"""
nome = 'Gustavo Guanabara'
idade = 25
peso = 74.5
print(nome, idade, peso)
#ERRORprint(nome + idade + peso)
"""
#########################################################
#interagindo com o usuario

nome = input('Qual seu nome: ')
idade = input('Quantos anos voce tem: ')
peso = input('Quanto voce pesa: ')
print(nome, idade, peso)