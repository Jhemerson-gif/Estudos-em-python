print(f'Bem vindo ao Conversor binario!')
num=int(input('Digite um numero inteiro: '))

print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO 
[2] converter para OCTAL 
[3] converter para HEXADECIMAL ''')

opção= int(input('Sua opção:'))


if opção == 1:
   print(f'{num} convertido para \033[31m BINÁRIO\033[m é igual a {bin(num)[2:]}')
elif opção == 2:
   print(f'{num} convertido para \033[31m OCTAL\033[m é igual a {oct(num)[2:]}')
elif opção == 3:
   print(f'{num} convertido para \033[31m HEXADECIMAL\033[m é igual a {hex(num)[2:]}')
else:
    print(f'Opção inexistente. Tente novamente!')
