import time
from time import sleep
valor = 0
print('-=-'*20)
print('\033[31mBEM VINDO A AGENCIA DE CALCULO\033[m')
print('-=-'*20)
tentativa = 1
escolha = 0
valor = int(input('Digite o primeiro numero: '))
valor2 = int(input('Digite  o segundo  numero:'))
sleep(2)

print('-=-'*20)
while escolha != 5:

    escolha = int(input('Escolha a operação matematica desejada: \n\033[31m[1]\033[mSomar \n\033[31m[2]\033[mMultiplicar \n\033[31m[3]\033[mMaior \n\033[31m[4]\033[mNovos numeros \n\033[31m[5]\033[mSair \n\033[1mOPÇÃO ESCOLHIDA: \033[m'))
    sleep(1)

    if escolha == 1:

        soma = valor + valor2
        print(f'A soma entre {valor} + {valor2} é igual a {soma}')
    elif escolha == 2:
        multiplicar = valor * valor2
        print(f'A  multiplicação entre {valor} x {valor2} é igual a {multiplicar}')
    elif escolha == 3:
        if valor2 > valor:
            print(f'O numero {valor2} é maior que o numero {valor}!')
        elif valor > valor2:
            print(f'O numero {valor} é mairo que o numero {valor2}!')
        else:
            print(f'Os numeros são iguais!')
    elif escolha == 4:
        print('Informe os números novamente:')
        valor = int(input('Digite o primeiro numero: '))
        valor2 = int(input('Digite o segundo numero: '))
    elif escolha == 5:
        print('Finalizando...')

    else:
        print('Opção invalida, tente novamente!')
    print('-=-'*20)




print('Fim de programa')