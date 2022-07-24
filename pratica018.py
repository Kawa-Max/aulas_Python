from time import sleep
from random import randint

print('-' * 10)
"""teste = []

# ---------------------------
# adicionando valores na lista
teste.append('Max')
teste.append(18)
# print(teste)
# ---------------------------
# jogando os valores em outra lista
# ---------------------------
galera = list()
galera.append(teste[:])  # --> adiciona os valores da variável teste dentro de galera, cria uma ligação entre as lista
#teste[0] = 'Maria'
#teste[1] = 22
# ---------------------------
  # --> Cria uma copia da Lista teste e cola em galera
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
# ---------------------------
print(galera)
# ---------------------------
"""
"""# _______________________________________________________
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45], ['Gustavo', 40]]
print(galera[0])  # --> ['João', 19]
print(galera[0][0]) # --> João
print(galera[2][1]) # --> 13
print('-' * 10)
#usando for

print('Com estrutura for: ')
print('Mostrando cada lista completa, dentro da lista composta')
for p in galera:
    print(p) # --> cada lista, dentro da lista
    sleep(0.1)
print()

print('Mostrando cada nome, dentro das listas que estão na lista composta')
for p in galera:
    print(p[0]) # --> Apenas os nomes(caso estejam na posição 0)
    sleep(0.1)
print()

print('Mostrando formatado: ')
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
    sleep(0.1)
print()
# _______________________________________________________
"""
#lendo valores e colocando nas listas

pessoal = []
dados = []
totmaior = totmenor = 0

for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    #dados.append(int(input('Idade: ')))
    dados.append(randint(9, 40))
    print(f'Idade: {dados[1]}')
    pessoal.append(dados[:])
    dados.clear() #--> apaga os valores da lista DADOS depois de adiciona-los na lista PESSOAL

for p in pessoal:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print(f'Temos um total de {totmaior} maiores e {totmenor} menores de idade')


"""
print('teste while:')

while True:
    dados.append(str(input('Nome: ')).title().strip())
    dados.append(randint(5, 65))
    print(f'Idade: {dados[1]}')
    pessoal.append(dados[:])
    dados.clear()
    cont = input('Quer continuar ?[S/N] ').upper().strip()[0]
    while cont not in 'SsNn':
        cont = input('\033[91mErro...\033[mQuer continuar ?[S/N] ').upper().strip()[0]
    if cont in 'Nn':
        break
"""

