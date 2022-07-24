frase = 'Curso em Video Python'
print(frase)
print(frase[3])  # quarta letra
print(frase[3:13])  # quarta letra ate o indice 13, parando no 12
print(frase[:13])  # do inicio ate o indice 13, parando no 12
print(frase[13:])  # começa no indice 13 e vai ate o final da string
print(frase[1:15])  # começa no indice 1 e vai ate o 15, parando no 14
print(frase[1:15:2])  # o de cima ate o 15, pulando de 2 em 2
print(frase[::2])  # inicio ate o fim, pulando de 2 em 2
print(frase.count('o'))  # quantas vezes tem a letra 'o' na string
print(frase.upper().count('O'))  # coloca a string em maiuscula e conta quantos 'O' aparece
print(len(frase))
print('Oi')
print("""kfhurhfsajhrifhsanchsagfsefbnsv ifhrbsc 
fbshjbsjkhcaiyvfa ufbshvchs csbfuwefs cbeufgjhv vuwefshv csfgweyf
HBDWEBFHS BCYSFBJCNSUCYhbdruvf vvryda vavjahfluvf 
hvryfvbreevj fdhvdjv aefgyurdvb dvryvf frvf
 hfmasbfiueavufyaevf svriufbeabbafdgvear fuarfbuerifwyfvwavf""")
# """ """ dentro de um metodo/funçao, converte um texto com varias linhas
# """ """ fora de um metodo/função é marcado como comentario
frase2 = '   Curso em video Python   '
print(len(frase2))
print(
    len(frase2.strip()))  # remove espaços do inicio e no fim da string e mostra seu comprimento apos a remoçao dos espaços
print(frase.replace('Python', 'Android'))  # substitui Python por Android
# frase[0] = 'J' - erro, pois nao é posivel substituir dessa forma
print('Curso' in frase)  # mostra se a palavra curso esta em frase
print(frase.find('Curso'))  # mostra a posiçao de curso em frase
print(frase.find('video'))  # erro,-1, pois n tem video com inicial minuscula na string
print(frase.lower().find('video'))  # converte a string para minusculo e mostra a posicao de video
print(frase.split())  # divide a string em varios pedaços, gerando uma lista
dividido = frase.split()  # coloca a frase dividida dentro da variavel 'dividido', gerando uma lista
print(dividido[0])  # dentro de dividido, mostre o indice 0
print(dividido[2][3])  # dentro de dividido 2, mostre a letra 3
