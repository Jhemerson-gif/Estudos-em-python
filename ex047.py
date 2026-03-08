print('Vou demonstrar entre 1 a 50 quais numeros são Par ou Impar! ')
pi= input('Escolha entre PAR OU IMPAR').upper()

if pi == 'PAR':
    for par in range(2,51,2):
        print(par, end=' ')
if pi == 'IMPAR':
    for impar in range(1,51,2):
        print(impar, end=' ')

