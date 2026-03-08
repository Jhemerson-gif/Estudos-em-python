from datetime import datetime
print('Vamos descobrir quantos de vocês já é maior de idade!')

atual = datetime.now().year

totmaior = 0
totmenor = 0

for c in range(1,8):
    ano= int(input(f'Digite o ano de nascimento da  {c} pessoa:'))

    idade = atual - ano

    if idade >= 21:
        totmaior += 1

    else :
        totmenor += 1

print(f'Ao todo tivemos {totmaior} pessoas maiores de idade!')
print(f'Ao todo tivemos {totmenor} pessoas menores de idade!')


