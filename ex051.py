from traceback import print_tb

print('Vamos ver a razão arítimetica !')
t= int(input('Digite o numero do seu Termo:')) # numero inicial da PA
r= int(input('Digite o numero da sua razão')) # numero de casas puladas da PA


print('Os 10 primeiros numeros da PA são:')
for c in range(t, (t+(10-1)*r)+r,r ):
    print(c, end=' ')
print(f'Acabou !')