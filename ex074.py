from random import randint
n = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
quantidade = 5
print('Os valores sorteados foram: ', end='')
for numeros in n:
    print(f'{numeros} ', end='')
print(f'\n O maior valor foi {max(n)}')
print(f' O menor valor foi {min(n)}')
