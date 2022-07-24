"""
    Funções (parte 1)

As FUNÇÕES em todas as linguagens de programação estão vinculadas a uma palavra magina: ROTINA

*ROTINA == COISAS QUE SÃO FEITAS CONSTANTEMENTE

O QUE VC FEZ CONSTANTEMENTE EM PYTHON ?

Desde o começo usamos FUNÇÕES, mesmo sem saber;

exemplo de FUNÇÕES existentes que usamos, desde o começo:

    print()  int()  str()
       len()   input()  sum()
           float()
"""

# Nem sempre só essas funções são o suficiente

# As DEF"S criam funções personalizadas, na qual VOCÊ personaliza

# A exemplo, podemos criar uma função para mostrar linhas,
# referente a usarmos linhas em praticamente todos os codigos

 #          mostraLinha()
"""

print('-----------------------------')
print('Sistema de alunos')
print('-----------------------------')

print('-----------------------------')
print('Cadastro de Funcionarios')
print('-----------------------------')

print('-----------------------------')
print('Jogo da Mega - Sena')
print('-----------------------------')

print('-----------------------------')
print('Erro de Sistema')
print('-----------------------------')

print('-----------------------------')
print('Titulos')
print('-----------------------------')

print('-----------------------------')
print('titulos')
print('-----------------------------')

podemos reduzir as linhas usando apenas um print criando uma def(função)

    |-->def mostraLinha():
    |       print('-----------------------------')-|
    |                                              |
    |---mostraLinha()                              |
        print('Sistema de alunos')  <--------------|
        mostraLinha()
        mostraLinha()
        print('Cadastro de Funcionarios')
        mostraLinha()
        mostraLinha()
        print('Jogo da Mega - Sena')
        mostraLinha()
        mostraLinha()
        print('Erro de Sistema')
        mostraLinha() 
"""
# entre a def's e seu programa principal, deve haver duas linhas vazias

# podemos também trabalhar com parametros

# podemos criar uma def personalizada que se adapte a nossas necessidades, usando parametros

"""
def mensagem(msg):
    print('----------------------')
    print(msg)
    print('----------------------')
    
    
mensagem('Sistema de Alunos')

def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)
    

titulo('Curso em video')
# assim, passamos uma mensagem como parametro(nesse tipo de caso, claro, podemos
 passar outros tipos de parametros tbm)
"""

"""
Empacotamento com Python

* --> desempacotar, conceito de usar varios parametros, sem saber a 
quantidade exata de parametros a ser passado, podemos usar dessa forma


--> def contador(*num):

# Usando varios parametros na def criada 

contador(5, 7, 3, 1, 4)
contador(8, 4, 7)

"""

