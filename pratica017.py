a = [2, 3, 4, 7]
#b = a #--> Cria uma ligação de 'a' com 'b'
#para criar uma copia sem alterar a lista a, usa-se o fatiamento
#ex:
b = a[:]
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b[2] = 8
print(b)



#isso n faz parte da aula, so chamei pra teste
#import random
#import time

#AULA PRÁTICA

#criando uma lista

#num = [2, 5, 9, 1]
"""#manipulando a LISTA
num[2] = 3
#error --> num[4] = 7
num.append(7) #--> correto
num.sort()
num.sort(reverse=True)
num.insert(2, 0)

"""
"""
#apagando itens na lista

del num[1]
num.pop(2)
num.remove(2) #--> elimina o primeiro valor 2 na lista

"""
# usando o IF para excluir um item dentro da lista
"""
if 5 in num:
    num.remove(5)
else:
    print('Não achei o valor 5 na lista')
"""

#mostrando a lista de forma mais 'bonita'
#valores = []
"""
valores.append(9)
valores.append(5)
valores.append(4)
print('Apenas os valores: ')
for v in valores:
    print(f'{v}...', end='')
print()
#ou tambem
print('Mostrando a posição e o valor: ')
for k, v in enumerate(valores):
    print(f'Na posição {k+1} encontrei o valor {v}!')
print('Fim da Lista')
"""
"""
print(num)
print(f'Essa lista tem {len(num)} elementos')
"""
"""
#lendo valores pelo teclado
for c in range(0, 15):
    valores.append(random.randint(0, 30))
    time.sleep(0.5)
print(valores)
print()

for k, v in enumerate(valores):
    print(f'Na posição {k+1} encontrei o valor {v}!')
    time.sleep(0.5)
print('Fim da Lista')"""



