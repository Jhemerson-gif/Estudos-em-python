print(f'\033[1:31m{ " Bem vindo a Banzai Store " :=^60}\033[m')
c= float(input('Qual o preço das compras ?'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a forma de pagamento?'))

if opção == 1:
    desconto= c-(c*0.10)
    dc= input('Dinheiro ou Cheque? ')
    if 'dinheiro':
        print(f'No pagamento em dinheiro no valor de R${c:.2f} oferecemos desconto de 10% totalizando R$ {desconto:.2f} ')

    elif'cheque':
        print(f'No pagamento em cheque no valor de {c:.2f} oferecemos desconto de 10% totalizando R$ {desconto:.2f} ')

if opção == 2:
    desconto= c-(c*0.05)
    print(f'No pagamento no cartão a vista  no valor de R${c:.2f} oferecemos desconto de 5% totalizando R$ {desconto:.2f} ')

if opção == 3:
    desconto= c/2
    print(f' No pagamento do cartão em 2x, não possuímos desconto totalizando o valor de R${c:.2f} em parcelas de 2x de {desconto:.2f}.' )

if opção == 4:
    desconto= c+(c*20/100)
    vezes= int(input('Escolha em quantas vezes de 3x a 10x :'))
    vt= desconto / vezes
    print(f'No pagamento do cartão em {vezes}x, o valor de R${c:.2f} há um acressimo juros de 20% totalizando R${desconto:.2f} as parcelas são de {vt} em {vezes}x !')

else:
    print(f'Opção invalida, tente novamente !')