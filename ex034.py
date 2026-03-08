'''salario=float(input('Digite o salario do funcionario que deseja da um aumento:'))
a= salario*0.10
aa= a+salario
b= salario*0.15
bb= b+salario
if salario =>1250:
    print(f'O salario do funcionario será de R$ \033[1:31m{aa:.2f}\033[m reais, um aumento de R$ \033[1:31m{a:.2f}\033[m reais')
else:
    print(f'O salario do funcionario será de R$ \033[1:31m{bb:.2f}\033[m reais, um aumento de R$ \033[1:31m{b:.2f}\033[m reais.')'''


#MÉTODO 2

salario=float(input('Digite o salario do funcionario que deseja da um aumento:'))
if salario <= 1250:
    novo= salario +(salario*15/100)
else:
    novo= salario + (salario*10/100)
print(f'Quem ganhava R$\033[31m{salario:.2f}\033[m passa a ganhar \033[33mR${novo:.2f}\033[m agora !')