num=int(input('Informe o seu numero: '))

u=num //1  % 10
d=num // 10 % 10
c= num // 100 % 10
m=num // 1000 % 10

print(f'Analisando o numero {num}')
print(f'O seu numero possui {u} Unidade')
print(f'O seu numero possui {d} Dezena')
print(f'O seu numero possui {c} Centena')
print(f'O seu numero possui {m} Milhar')