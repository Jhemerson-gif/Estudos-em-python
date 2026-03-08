lista = []
impar = []
par =[]
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
    if valor % 2 == 0:
        par.append(valor)


    if valor % 2 == 1:
        impar.append(valor)

print('-='*40)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')


#Exemplo do professor

'''while True:
    lista.apend(int(input('Digite um valor: ')))
    resp= str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)

print('-='*40)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')    '''

