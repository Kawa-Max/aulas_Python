"""
Variaveis compostas - LISTAS(parte 1)

teoria:

nas listas, usa-se '[]'(tuplas usa '()')
Listas podem ser alteraveis/mutaveis
ex:
    lanche = ['hamburguer', 'suco','pizza','pudim']
    lanche[3] = 'picole'

PARA ADICIONAR UM ELEMENTO NO FINAL DA LISTA, USA-SE O COMANDO .append()
ex:
    lanche.append('cookie')

PARA ADICIONAR ALGUM ELEMENTO EXTRA EM UMA POSIÇÃO DETERMINADA, USA-SE O COMANDO .insert()
ex:
    lanche.insert(0, 'hot-dog')

PARA APAGAR UM ITEM DENTRO DA LISTA, USA-SE O COMANDO del, pop ou remove

del lanche[3] - apaga o item selecionado dentro da lista
lanche.pop() - apaga o ultimo item ou o item escolhido
lanche.remove('pizza') - remove um item na lista pelo 'nome', sem precisar usar o indice

'os comandos elimina o indice, e reorganiza a lista'

"""

"""
para saber se um item está na lista, e depois 'remove-lo', usa-se o comando if

if 'pizza' in lanche:
    lanche.remove('pizza')
"""

"""
usando lista com range, para gerar valores
valores = list(range(4, 11))
print(valores)
#o range cria os valores já em ordem
"""
#atribuindo valores na lista
"""
valores = [8, 2, 5, 4, 9, 3, 0] --> Lista aleatoria
valores.sort() --> coloca a lista em ordem
valores.sort(reverse=True) --> coloca a lista em ordem, de traz para frente
 e para saber o tamanho de uma lista, usa-se a função len()
len(valores) --> retornaria o valor 7 

"""

