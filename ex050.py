cont = 0
soma= 0
for c in range(1, 7):
    n= int(input('Digite um numero:'))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Esses são os numeros pares, foram considerados {cont} numeros pares!\nA soma dos numeros pares é {soma}')

