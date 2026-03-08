
n= (int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o ultimo número: '))
    )



print(f'VocÊ digitou {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 apareceu {n.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end='')
for numero in n:
    if numero % 2 == 0:
        print(numero, end=' ')
