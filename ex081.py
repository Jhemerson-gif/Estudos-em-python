lista =[]
posições= []
while True:
    valor = int(input('Digite um valor:'))
    lista.append(valor)
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()

    if continuar in 'N':
        break
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}')

for indice, valor in enumerate(lista):
    if valor == 5:
        posições.append(indice)

if posições:
    print(f'O valor 5 apareceu na posição {posições} ')
else:
    print(f'O valor 5 não apareceu na lista !')

#Opcional e maiks elegante  do professor.
#Mas o meu indica especificamente a posição sendo até mais preciso !

'''if 5 in lista:
    print(f'O valor 5 apareceu na posição {posições} ')
else:
    print(f'O valor 5 não apareceu na lista !')'''