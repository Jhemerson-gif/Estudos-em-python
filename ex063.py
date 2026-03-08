print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
termo =int(input('Quantos termos você quer mostrar? '))
cont = 3
t1 = 0
t2 = 1

print(f'{t1} -> {t2} ', end='')
while cont <= termo:
    fibonacci = t1 + t2
    cont+=1
    print(f'-> {fibonacci} ', end='')
    t1 = t2
    t2 = fibonacci

print('FIM')
