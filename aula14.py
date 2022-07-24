"""
Laço de repetição(parte 2)
com while, nao precisa determinar um range
ESTRUTURA DE REPETIÇÃO com teste logico: WHILE

enquanto
      \
       \ |
     __>/\ nao maça_
    |   \/         |
    |___|passo     |
           ________|
          |
          |pega

algoritmo

enquanto nao maça
    passo
pega
-------------------
em pyhton

while not maça:
    passo
pega

"""
"""
situação 1:

algoritmo:

enquanto nao maça
    se chao
        passo
    se vazio
        pula
    se moeda
        pega
pega

em python:

while not maça:
    if chao:
        passo
    if vazio:
        pula
    if moeda:
        pega
pega

"""
