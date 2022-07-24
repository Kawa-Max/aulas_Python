"""
FUNÇÕES (parte 2)

-----------topicos da aula----------------
                                          |
1 - Interactive Help = Ajuda interativa   |
                                          |
2 - Docstrings                            |
                                          |
3 - Argumentos Opcionais                  |
                                          |
4 - Escopo de váriaveis                   |
                                          |
5 - Retorno de resultados                 |
-----------------------------------------
"""
# --------------------------------------------------------------------
# 1 - Usado para ver o 'manual' de uma função ou biblioteca,
# geralmente usado no console do pycharm, usando o comando 'help()'
# também pode ser acessado usando o print(input.__doc__)
# --------------------------------------------------------------------
# 2 - Podemos criar nossas proprias docstrings
# docstrings entram logo apos a criação da def
# Para fazer uma docstringe é so abrir " 3 vezes ("""""")
# e entt configuramos nossa docstring
'''

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: sem retorno
    Função criada durante os estudos com o Curso em Video
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim !')


help(contador)
contador(2, 10, 2)
'''

# 3 - Passando parâmetros opcionais
# para um parametro ser opcional, é só ter um parametro sendo '=0'

# ex:
'''

def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: Primeiro valor
    :param b: Segundo valor
    :param c: Terceiro valor
    :return: sem retorno
    Função criada durante os estudos com o Curso em Video
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(b=4, c=2)
somar(c=3, a=2)
somar()
'''

# 4 - Onde a variavél nasce, e onde ela morre
# Variaveis dentro de def's, tem ESCOPO LOCAL
# Variaveis criadas fora de def's, tem ESCOPO GLOBAL
'''
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa principal
n = 2
print(f'No programa principal, n vale {n}')
print(f'No programa principal, x vale {x}')

 ----------------------------------
|  -------------------------------  |
| |def teste(b):                  | |
| |    a = 8                      | |
| |    b += 4                     | |                   a[8]
| |    c = 2                      |-------> Escopo      b[9]
| |    print(f'A dentro vale {a}')| |           local   c[2]
| |    print(f'B dentro vale {b}')| |                           
| |    print(f'C dentro vale {c}')| |
| |-------------------------------| |
|                                   |
| a = 5                             |-------> Escopo global   a[5]
| teste(a)                          |
|print(f'A foram vale {a}')         |
|print(f'B dentro vale {b}') }  erro|
|print(f'C dentro vale {c}') }  erro|
|-----------------------------------|
'''

# teste
"""
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')"""

# tratando variavéis globais, como globais, é so usar a palavra 'global' seguida da variavel global que deseja usar,
# dentro da def
'''
def teste(b):
    global a
    a = 8 
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
print(f'A fora vale {a}')
print(f'B fora vale {b}')
print(f'C fora vale {c}')
'''

# 5 - Para retornar valores, usa-se o codigo return


def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: Primeiro valor
    :param b: Segundo valor
    :param c: Terceiro valor
    :return: A soma dos valores
    Função criada durante os estudos com o Curso em Video
    """
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os resultados foram {r1} {r2} {r3}')
