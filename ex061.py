print('Gerador de PA')
print('-'*10)
n=int(input('Primeiro termo: '))
razao=int(input('Digite a razão: '))
termo = n
c = 1
mais = 10
total = 0
print('Os 10 primeiros numeros da PA são:')
while mais != 0:
    total += mais
    while c <= total:
        print(f'{termo}',end='')
        print(f' -> ', end='' )
        termo += razao
        c+=1
    print('Pausa')
    mais=int(input('Quantos termos você quer mostrar a mais?'))


print(f'Progressão finalizada com {c} termos mostrados')
print('FIM')