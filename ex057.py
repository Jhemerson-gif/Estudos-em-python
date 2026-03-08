c = 'N'

while c == 'N':
    sexo = str(input('Digite o seu Sexo: [M/F] ')).strip().upper()[0]

    while sexo not in ['M', 'F']:

        sexo = str(input('Sexo incorreto, Digite novamente:')).strip().upper()


    c = str(input(f'Sexo é {sexo} está correto ?')).upper()

    while c not in ['S', 'N']:
        c = str(input('Ok, digite novamente [S/N]:')).upper()

    if sexo == 'M':
        print('Sexo Masculino')
    elif sexo == 'F':
        print('Sexo Feminino')

print('Fim')