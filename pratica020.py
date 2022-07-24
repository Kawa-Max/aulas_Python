# --> Tudo dentro das double-aspas representa as partes repetitivas, que podem virar uma def(função)

# soma é a função que sera criada

"""
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)
"""

"""
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print()


# programa Principal
soma(4, 5)      # }
soma(8, 9)      # } nao explicitado
soma(2, 1)      # }
# soma(4) --> erro, pois a nossa função prescisa de 2 parametros e estamos passando apenas 1
soma(b=1, a=3)  # explicitado

# soma(3, 9, 5) --> Erro, não podemos ter 3 parametros em uma função de 2


def contador(*num):
    # print(num)
    tam = len(num)
    for valor in num:
        print(valor, end=' ')
    print()
    print(f'recebi os valores {num} e são {tam} numeros')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
"""
"""
# um ultimo exemplo aleatorio


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

"""


def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(1)
soma(5, 2)
soma(2, 9, 4)
