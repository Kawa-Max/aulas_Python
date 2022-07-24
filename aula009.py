"""
------------------------------
  Manipulando cadeias textos
------------------------------
#teoria
______________________________________________________________________________________
Curso em video python (string)

-toda cadeia de caractere/string está entre ' '(aspas) ou " "(aspas duplas)
- range(o ultimo valor nao é contado)
'Curso em video python'
atribuir a uma variavel
- frase = "Curso em Video de Python"
cria um espaço na memoria do computador, e cada letra recebe um indice começando de 0
--------------------------------------------------------------------------------------
-Fatiamento = frase[9](estrutura de lista) - 'V' (indice dentro da string)
            = frase[9:13] - (começa no 9 e vai ate o 13, excluindo o 13) - "V i d e"
            = frase[9:21] - (Fatia ate 21, ignirando o 21) - "V i d e o  P y t h o n"
            = frase[9:21:2] - (fatiamento de 9 ate 21, pulando de 2 em 2) - "V d o P t o"
            = frase[:5] - (vai do inicio ate o 5, ignorando o 5) - "C u r s"
            = frase[15:] - (vai do 15 ate o final da string) - "P y t h o n"
            = frase[9::3] - (começa do 9 e vai ate o final, pulnado de 3 em 3) - "V e P h"
---------------------------------------------------------------------------------------
-Analisar   = metodo len() - comprimento = len(frase) - 21(tamanho da string da variavel frase)
            = frase.count('o') - conta quantas vezes existe a letra 'o' - 3
            = frase.count('o', 0, 13) - vai do 0 ate o 13 e conta quantos 'o' tem - 1
            = frase.find('deo') - mostra em que momento começa 'deo' - indice 11 ate 13
            = frase.find('Android') - retorna o valor -1, caso a string n exista
            = 'Curso' in frase - in == existe curso em frase - True
---------------------------------------------------------------------------------------
-Transformaçao  = frase.replace('Python','Android') - substitui a string de forma secundaria
                = frase.upper() - coloca a string em MAIUSCULO - CURSO EM VIDEO PYTHON
                = frase.lower() - coloca a string em miusculo - curso em video python
                = frase.capitalize() - coloca todo caracterer em minusculo mantendo a primeira em maiuscula
                (pega a string inteira e joga em minusculo, mantendo o indice 0 em maiuscula)
                = frase.title() - transforma o caractere inicial apos o espaço em maiusculo
        [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
frase = '   Aprenda Python  '
        frase.strip() - elimina espaços inuteis
        frase.rstrip() - remove espaços da direita (final)
        frase.lstrip() - remove espaços da esquerda (inicio)
---------------------------------------------------------------------------------------------
-Divisa     = frase.split() - cria divisoes na string, gerando uma lista separando a string em varias strings
---------------------------------------------------------------------------------------------
- Junçao    = '-'.join(frase) - gera uma string juntando tudo, separando por "-"(traços)
______________________________________________________________________________________

"""