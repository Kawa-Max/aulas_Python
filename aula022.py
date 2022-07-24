"""
     Módulos e Pacotes
                        """
'''
        Modulos
        
 -----------------------------------------------
| Modularização --> ato de construir módulos    |
|   - Surgiu no inicio da década de 60          |
|   - Sistema ficando cada vez maiores          |
|   - Foco: dividir um programa grande          |
|   - Foco: aumentar a legibilidade             |
|   - Foco: facilitar a manutenção              |
 -----------------------------------------------



 -----------------------------------------
|def fatorial(n):                         |
|    f = 1                                |
|    for c in range(1, n+1):              |
|       f *= c                            |
|    return f                             |
|                                         |
|                                         |
|def dobro(n):                            |
|    return n * 2                         | --> O 'Projeto principal' com Funções e o código principal no mesmo lugar
|                                         |
|                                         |
|def triplo(n):                           |
|    return n * 3                         |
|                                         |
|                                         |
|num = int(input('Digite um valor: '))    |
|fat = fatorial(num)                      |
|print(f'O fatorial de {num} é {fat}')    |
 -----------------------------------------


# Podemos pegar todas as funções e colocar em outro arquivo

 -----------principal.py------------------------
|import uteis                                   |
|                                               |
|num = int(input('Digite um valor: '))          | --> Programa Principal
|fat = uteis.fatorial(num)                      |
|print(f'O fatorial de {num} é {fat}')          |
|print(f'O dobro de {num} é {uteis.dobro(num)}')|
 -----------------------------------------------
                                         ----------------uteis.py-----------------
                                        |def fatorial(n):                         |
                                        |    f = 1                                |
                                        |    for c in range(1, n+1):              |
                                        |       f *= c                            |
                                        |    return f                             |
                                        |                                         |
                                        |                                         |
                                        |def dobro(n):                            | --> programa separado com as funções 
                                        |    return n * 2                         |                                                                                      
                                        |                                         |
                                        |                                         |
                                        |def triplo(n):                           |
                                        |    return n * 3                         |
                                        |                                         |
                                         -----------------------------------------
                                         
no programa principal podemos 'chamar' as funções de outra forma também;
porém, o PYCHARM NÃO RECOMENDA UTILIZAR MODULOS DESSA FORMA, POIS PODE 
HAVER CONFLITOS, INCOMPATIBILIDADE caso seu programa principal tenha mais
de um pacote/modulo com funções de MESMO NOME, isso pode gerar conflitos na 
execusão do código
Normalmente, será execultado a ultima importação

 -----------principal.py------------------------
|from uteis import fatorial, dobro              |
|                                               |
|num = int(input('Digite um valor: '))          | --> Programa Principal usando o 'from' na hora de importar o modulo/
|fat = fatorial(num)                            |     pacote criado
|print(f'O fatorial de {num} é {fat}')          |
|print(f'O dobro de {num} é {dobro(num)}')      |
 -----------------------------------------------

exemplo:

from uteis import fatorial
from math import sqrt
from datetime import datetime
from random import randint


  Vantagens da Modularização

- Organização do código
- Facilidade na manutenção
- Ocultação de códigos detalhado
- Reutilização em outros projetos

'''
"""
        Pacotes     

 ----------------uteis.py----------------------------------
| --numeros------     ----datas-------  ------cores-----    |
|| def's criadas |   |  def's criadas ||  def's criadas |   |
| ---------------     ----------------  ----------------    |
|                                                           |
| ----strings-----                                          |
|| def's criadas  |                                         |       import uteis
| ----------------                                          |           ou 
 -----------------------------------------------------------        from uteis import datas

Dentro do python, todo arquivo .py é um modulo e toda 'pasta' é um pacote

todo pacote, tem que ter um arquvio chamado '__init__.py' 

uteis
 |__init__.py
 |
 |--numeros
 |      __init__.py
 |--datas
 |      __init__.py
 |--cores
 |      __init__.py
 |--strings
 |      __init__.py
"""
'''
Para criar pacotes;

    Botão direito no projeto --> New --> Python Package
    
Importando;

    from uteis import numeros

'''
