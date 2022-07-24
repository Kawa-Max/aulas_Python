"""
Variavéis Compostas - Dicionários

Podemos criar INDICES LITERAIS, podemos personalizar os indices nos dicionarios

DICIONARIOS EM PYTHON SÃO IDENTIFICADOS COM {} OU DICT()

ex:

dados = dict()
dados = {'nome': 'Pedro', 'idade': 25 }
print(dados['nome']) --> Pedro
print(dados['idade']) -> 25

para adicionar itens:

dados['sexo'] = 'M', o proprio python já cria o elemento sexo dentro do dicionario

para remover itens usamos o comando del:
del dados['idade']

"""
"""
filme = { 'titulo': 'Star Wars',
          'ano': 1977,
          'diretor': 'George Lucas'
}

print(filme.value()) --> pega todos os valores do dicionarios 'Star Wars', 1977, 'George Lucas'

print(file.keys()) --> pega as chaves do dicionario 'titulo','ano','diretor'

para pega tudo de uma vez

print(filme.items())


"""
#Usando laços de repetição
"""
for k, v in filme.items():
    print(f'O {k} é {v}') --> O 'titulo' é 'Star Wars'
                          --> O ano é 1977
                          --> 0 diretor é George Lucas
"""

#PODEMOS USAR EM CONJUNTO AS TUPLAS, LISTAS E OC DICIONARIOS:

"""
EX: 
    locadora = [
indice 0  ----> {'titulo': 'Star Wars','ano': 1977,'diretor': 'George Lucas'},
indice 1  ----> {'titulo': 'Avengers','ano'2012: ,'diretor': 'Joss Whedon'},
indice 2  ----> {'titulo': 'Matrix','ano': 1999 ,'diretor': 'Wachowski'}
                ]

#indice se refere a lista, tudo dentro de {} é dicionario, dentro do [] é a lista 

mostrando os resultados 

print(locadora[0]['ano']) --> 1977
print(locadora[2]['titulo']) --> Matrix
"""