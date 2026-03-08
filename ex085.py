numero=[]
pa=[]
impar=[]

for c in range (1,8):
    numero.append(int(input(f'Digite o {len(numero)+1}o. valor:')))

for c in numero:
    if c % 2 == 0:
        pa.append(c)
    else:
        impar.append(c)

print('-=' *40)
print(f'Os valores pares digitados foram: {sorted(pa)}')
print(f'Os valores impares digitados foram: {sorted(impar)}')
 