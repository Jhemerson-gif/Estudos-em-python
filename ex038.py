print(f'Vamos comparar os numeros e descobrir qual o maior !')

n= int(input('Digite um numero :'))
n1= int(input('Digite outro numero :'))

if n>n1:
    print(f'O Numero {n} é maior que o numero {n1}')
elif n<n1:
    print(f'O Numero {n1} é maior que o numero {n}')
else:
    print(f'Não existe valor maior,os numeros são iguais !')
