from random import randint


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


# num = int(input('Digite um valor: '))
num = randint(0, 1000)
print(f'\033[34mDigite um valor: \033[96m{num} ')
if par(num):
    print('\033[32mÉ par')
else:
    print('\033[31mNão é par, É ìmpar')


"""
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um numero e veja seu fatorial: '))
print(f'O fatorial de {n} é {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
num = randint(0, 10)
f4 = fatorial(num)

print(f'5! = {f1}\n4! = {f2}\n ! = {f3}\n{num}! = {f4}')
"""