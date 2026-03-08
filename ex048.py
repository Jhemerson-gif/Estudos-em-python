print('Irei demonstrar os numeros que são divisiveis de 3')


print('Este são todos os numeros divisiveis entre 1 a 500')
soma= 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont= cont + 1
        soma = soma + c


print(f'A soma de todos os  {cont} valores solicitados é {soma}')
