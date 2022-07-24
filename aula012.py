
"""
CONDIÇÕES ANINHADA - colocar uma coisa dentro da outra
dentro de um if, pode-se usar quantos elif's quiser, porém, apenas 1 else
nunca iniciar um elif sem um if
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

    Condição composta
        carro.siga()
            |
    --------_____________|___________
    |              carro.siga()      |
carro.siga()            |    .carro.siga()
carro.direita()         |    .carro.esquerda()
carro.siga()            |    .carro.siga()
carro.direita()         |    .carro.esquerda()
carro.esquerda()        |    .carro.siga()
carro.siga()            |            |
carro.direita()         |            |
carro.siga()            |            |
    |                   |            |
    |                   |            |
    _________________Pare()___________

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
senao se carro.direita()
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
senao
    carro.siga
carro.pare()
-------------------------------
representando em python
carro.siga()
if carro.esquerda():
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
elif carro.direita():
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
else:
    carro.siga
carro.pare()
--------------------------------
if carro.esquerda():
    bloco_1
elif carro.direita():
    bloco_2
else:
    bloco_3
¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
if carro.esquerda():
    bloco_1

elif carro.direita():
    bloco_2

elif carro.ré():
    bloco_3

else:
    bloco_4
"""
