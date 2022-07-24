"""
laços, repetições ou iterações

LAÇO DE REPETIÇÃO (parte 1):
_______________________________________________
    Estrutura de repetição (laço) : FOR
-------------------
1° situação

escrevendo o algoritmo:
    |passo
    |passo
    |passo
    |passo
    |passo
    |pega
-------------------
     |
  -> [] 1 -> 10-|
 |___|passo     |
        ________|
       |
       pega
estrutura:

laço c no intervalo(1, 10)
    passo
pega

em python:

for c in range(1, 10):
    passo
pega
______________________________________
2° situação

|passo
|pula
|passo
|pula
|passo
|pula
|passo
|pega

      |
  -> [] 0 -> 3- |
 |   |passo     |
 |___|pula      |
        ________|
       |
       |passo
       |pega

    escrevendo o algoritmo:

    laço c no intervalo(0, 3)
        passo
        pula
    passo
    pega

    em python:
    for c in range(0, 3):
        passo
        pula
    passo
    pega
---------------------------------------
3° situação

    escrevendo algortimo:

    laço c no intervalo(0,3)
        se moeda
            pega
        passo
        pula
    passo
    pega

    em python
    for c in range(0,3):
        if moeda:
            pega
        passo
        pula
    passo
    pega
----------------------------------------
_______________________________________________

"""