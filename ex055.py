pesomaior = 0
pesomenor = 0


for p in range(1, 6):
    peso = float(input(f'Peso da {p} pessoa:'))

    if p == 1:
        pesomaior= peso
        pesomenor = peso

    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso


print(f'O maior peso lido foi {pesomaior}')
print(f'O menor peso lido foi {pesomenor}')
