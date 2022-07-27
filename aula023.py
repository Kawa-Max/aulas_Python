"""
        Tratamentos de Erros e Exceções

 - ERROS ACONTECEM NA VIDA, EM SOFTWARES, EM PYTHON, ETC.... SEMPRE
 -------------------------------------------------------
| Exemplo de erros de sintaxe no Pytho:                 |
|                                                       |
|    primt(x)                                           |
|    print(x)                                           |
|                                                       |
| Erros sintaticos é apenas um tipo de erro que existe  |
| O erro é não inicializar a variavél x, e a escrita    |
| errada                                                |
 -------------------------------------------------------

 NameError       --> erro de nome


 ValueError      --> erro de valor


 TypeError       --> erro de tipo
        r = 2 / '2'

 ZerDivisionErro --> Erro na divisão por 0


 IndexError        --> erro de index
         lst = [3, 6, 4]
        print(lst[3])

 O Python tem uma diversidade de erros

 Exception --= exceção

 Para tratar erros e exceções, usamos o comando Try e except
_____________________________________________________________
 ex:

    try:
        operação

    except:
        falhou

    else:
        deu certo

    finally:
        acontece independente se der certo ou errado

_____________________________________________________________

exemplo pratico:

Sem tratamento de erro

    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
    print(f'O resultado é {r} ')

Com tratamento de erro

    try:
        a = int(input('Numerador: '))
        b = int(input('Denominador: '))
        r = a / b

    except Exception as erro:
        print(f'O problema encontado foi {erro.__class__} ')

        #print('Infelizmente tivemos um problema :(')

    else:
        print(f'O resultado é {r:.1f}')

    finally:
        print('Volte sempre obrigado')

todos TRY pode ter varios except

++++++++++++++++++======================+++++++++++++++++++++++++++++

Com tratamento de erro usando varios except:

    try:
        a = int(input('Numerador: '))
        b = int(input('Denominador: '))
        r = a / b

    except (ValueError, TypeError):
        print(f'Tivemos um problema com os tipos de dados digitados')

    except ZeroDivisionError:
        print('Não é possível dividir por zero')

    except KeyboardInterrupt:
        print('O usuario preferiu não informar os dados!')

    except Exception as erro:
        print(f'O erro encontrado foi {erro.__class__}')

    else:
        print(f'O resultado é {r:.1f}')

    finally:
        print('Volte sempre obrigado')

++++++++++++++++++======================+++++++++++++++++++++++++++++



------------------------------------------------------------

"""


