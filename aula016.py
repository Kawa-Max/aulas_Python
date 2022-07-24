"""
Variaveis Compostas - Tuplas

AS TUPLAS SÃO IMUTÁVEIS - Não pode-se mudar uma Tupla enquanto o programa estiver sendo execultado
apenas é possivel, caso faça alterações no codigo, mudando os valores da Tupla

teoria:

quando uma variavél simples é declarada, ela se torna um espaço na memoria docomputador
ex: lanche = hamburguer
caso a mesma variavel receba outro parametro ao decorrer do codigo, o proximo parametro substitui o
primeiro
ex lanche = hamburguer
   lanche = suco

para ter mais de um espaço com variavel, uma das formas é usando TUPLAS, LISTAS OU DICIONARIOS,
criando uma variavél composta. Elas podem guardar varios parametros, varios itens.
nessa aula usaremos TUPLAS

ex lanche = hamburguer, suco, pizza, pudim
INDICES =       0        1      2     3

-----------------------------------------
FATIAMENTO:

    print(lanche[2]) pizza      - pega o indice 2 na tupla
    print(lanche[0:2]) hamburguer, suco     - começa em 0 e vai ate 2, ignorando o 2
    print(lanche[1:]) suco, pizza, pudim    - vai do indice 1 ate o fim
    print(lanche[-1]) pudim     - ultimo elemento

Usando laço de repetição

|-->for c in lanche:--|
|-----print(c)  <-----|
        |
     hamburguer
     suco
     pizza
     pudim

-----------------------------------------


"""