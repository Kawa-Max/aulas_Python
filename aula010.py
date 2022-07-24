"""
CONDIÇOES SIMPLES E COMPOSTAS

teoria:
    condição simples
        carro.siga()
        carro.esquerda()
        carro.siga()
        carro.direita()
        carro.siga()
        carro.direita()
        carro.siga()
        carro.esquerda()
        carro.siga()
        carro.pare()

estrutura simples, execultado de cima pra baixo, da esquerda pra direita

    Condição composta
        carro.siga()
            |
    --------_________________________
    |                               |
carro.siga()                .carro.siga()
carro.direita()             .carro.esquerda()
carro.siga()                .carro.siga()
carro.direita()             .carro.esquerda()
carro.esquerda()            .carro.siga()
carro.siga()                        |
carro.direita()                     |
carro.siga()                        |
    |                               |
    |                               |
    _____________Pare()_____________

comando siga() e pare(), ssempre acontece, independente da escolha de direção

a escolha é verificada a partir do comando se, e senão
representando estruturada em python:

------------------------------
carro.siga()
se carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
senao
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
carro.pare()
--------------------
se carro.esquerda()
    bloco __V__
senao
    bloco __F__
-------------------------------------
em ingles, como usaremos nos scripts

CONDIÇÃO

if carro.esquerda():
    bloco True
else:
    bloco False
-------------------------------------
Somente 'if' para estrutura simples
e 'if' 'else' para estruturas compostas
----------------------------------------
ex:
tempo = int(input('Quantos anos tem seu carro ? '))
if tempo <= 3:
    print('Seu carro está novo ainda')
else:
    print('Seu carro ja está velho')
print('__FIM__')
"""

"""
todo comando colado no lado esquerdo, sempre execulta, no lado direito execulta-rá 
dependendo da escolha ou condiçao
-----------------------------------------------------------------------------------
tempo = int(input('Quantos anos tem seu carro: '))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')
-----------------------------------------------------------------------------------
"""
"""
#exemplos praticos
#ESTRUTURA SIMPLES IF
nome = str(input('Qual seu nome ? ')).capitalize()
if nome == 'Max': #INICIO DA ESTRUTURA
    print('Que nome lindo esse.')   #BLOCO VERDADEIRO
print('Bom dia, {}!'.format(nome))

#ESTRUTURA COMPOSTA

nome = str(input('Qual seu nome ? ')).capitalize()
if nome == 'Kawã max': #INICIO DA ESTRUTURA
    print('Que nome lindo esse.')   #BLOCO VERDADEIRO
else:
    print('Seu nome é tão normal')
print('Bom dia, {}!'.format(nome))
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A sua media foi {:.1f}'.format(media))
if media >= 6:
    print('Sua media foi boa! Parabéns')
else:
    print('Sua media foi ruim, estude mais')
"""
-------------------------------
CONDIÇÃO SIMPLIFICADA:
 
print('PARABENS' if media >= 6 else 'ESTUDE MAIS')
-------------------------------
"""