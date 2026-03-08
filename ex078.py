'''valores = []
maior=0
menor= 0

for cont in range(0,5):
    valores.append(int(input(f'Digite o {cont+1}° valor: ')))

    if cont == 0:
        menor=maior=valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]

print(f'Os valores digitados foram: {sorted(valores)}')
print(f'O maior valor digitado foi {maior} ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ',end='')
print()
print(f'O menor valor digitado foi {menor} ',end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ',end='')
print()'''



valores = []
maiorvalor=[]
menorvalor=[]

for cont in range (1,6):
    valores.append(int(input(f'Digite um valor: ')))

for posi, valor in enumerate(valores):
    if valor  == max (valores):
        maiorvalor.append(posi)

    if  valor == min(valores):
        menorvalor.append(posi)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)}... na posição {maiorvalor}...')
print(f'O menor valor digitado foi {min(valores)}... na posição {menorvalor}...')
