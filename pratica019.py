# PARTE PARTICA
#               <<<<<<<<<<<<<DICIONARIOS>>>>>>>>>

pessoas = {
    'nome': 'Gustavo',
    'sexo': 'M',
    'idade': 22
}
"""
# print(pessoas[0]) --> erro
print(pessoas['nome'])  # --> indice nome no dicionario
print(pessoas['idade'])  # --> indice idade no dicionario
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')  # --> indice nome e idade formatado
print(pessoas.keys())  # --> chaves atribuidas em pessoas (nome, sexo, idade)
print(pessoas.values())  # -->  valores atribuidos as chaves ('Gustavo','M',22)
print(pessoas.items())  # --> todos os itens presente no dicionario
"""
# ----------------------------------------------------------------------------------------------------------------------
# acessando os valores com for
"""#apagando
#del pessoas['sexo']

#modificando
pessoas['nome'] = 'Leandro'

#adicionando
pessoas['peso'] = 98.5
for k in pessoas.keys():
    print(f'{k} ', end='')
print()
print()
for v in pessoas.values():
    print(f'{v} ', end='')
print()
print()
for k, v in pessoas.items():
    print(f'chave: {k} // valor: {v}')
"""

"""# usando dicionários dentro de listas

brasil = []

estado1 = {
    'uf': 'Rio de Janeiro', 'sigla': 'RJ'
}
estado2 = {
    'uf': 'São Paulo', 'sigla': 'SP'
}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])"""

#lendo valores ejogando nos dict's

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['Uf'] = input('Unidade Federativa: ').title()
    estado['Sigla'] = input('Sigla do estado: ').upper()
    #brasil.append(estado) --> error
    # brasil.append(estado[:]) --> error
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end='')
    print()
    """for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
        print()
    """