"""
Variáveis Compostas - LISTAS(parte 2)

listas compostas

pode-se copiar os itens de uma lista, e colocar em outra lista
-----------------------------------------------------------------
ex:
    dados = [] ou list()
    pessoas = [] ou list()
    #adicionando itens na lista DADOS
    dados.append('Pedro')
    dados.append(25)

    #copiando a lista e colocando dentro de PESSOAS
    pessoas.append(dados[:])

Assim eu tenho uma lista(dados) dentro de outra lista(pessoas)
------------------------------------------------------------------
pessoas:
 ---------------------------------------------------
|    ------------- | ------------- | -------------  |
|   |'Pedro' | 25 ||| 'Maria' | 19||| 'João' | 32 | |
|    ------------- | ------------- | -------------  |
|       0     1    |     0     1   |    0      1    |
----------------------------------------------------
        0               1                2

pessoas = [['Pedro', 25],['Maria', 19],['João', 32]] --> estrutura da lista composta

mostrando os valores com fatiação:

print(pessoas[0][0]) --> Pedro, dentro da lista pessoas, pega o indice 0 que tbm é uma lista e busca o indice 0
print(pessoas[1][1]) --> 19, dentro da lista pessoas, pega o indice 1 que tbm é uma lista e busca o indice 1
print(pessoas[2][0]) --> João, dentro da lista pessoas, pega o indice 2 que tbm é uma lista e busca o indice 0
print(pessoas[1]) --> ['Maria', 19], dentro da lista pessoas, pega o indice 1
"""