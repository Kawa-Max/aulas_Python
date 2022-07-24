nome = str(input('Qual seu nome ? '))
if 'Max' in nome:
    print('Que nome maravilhoso')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem normal no Brasil')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Que belo nome feminino')
else:
    print('Que nome normalzinho...')
print('Tenha um bom dia, {}'.format(nome))

