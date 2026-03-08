print('='*40)
print('{:^40}'.format('\033[1mBANCO CEV\033[m'))
print('='*40)

valor = int(input('Que valor vocÊ quer sacar? R$'))
total = valor
céd = 200
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd +=1
    else:
        if totcéd > 0:
            print(f'O total de {totcéd} cédulas de R${céd}')
        if céd == 200:
            céd = 100
        elif céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 1
        totcéd = 0
        if total == 0:
            break


print('='*50)
print('Volte sempre ao BANCO CEV ! Tenha um bom dia !')
print('='*50)

