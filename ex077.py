lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHOM', 'CURSO', 'GRÁTIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGAMADOR', 'FUTURO')

for item in lista:
    print(f'\nNa palavra {item.upper()} temos ',end='')
    for vogais in item:
        if vogais.lower() in 'aãâáàeêéèiîíìõôóòuûúÙ':
            print(vogais, end=' ')
