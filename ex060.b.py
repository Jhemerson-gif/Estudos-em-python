n = int(input('Digite um numero para calcular o fatorial: '))
c = n
f = 1
for c in range (n, 0, -1  ):
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f *= c

print(f'{f}')