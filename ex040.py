print(f'Vamos Calcular as notas !')
nome= input('Digite o nome do aluno:')
n= float(input('Digite a nota do aluno no primeiro semestre :'))
n1= float(input('Digite a nota do aluno no segundo semestre'))
n2= float(input('Digite a nota do aluno no terceiro semestre'))
n3= float(input('Digite a nota do aluno no quarto semestre'))
m= (n+n1+n2+n3)/4

if m < 5 :
    print(f'A nota do aluno {nome} é de {m} está abaixo da média e está \033[1:31mREPROVADO!\033[m')

elif m < 6.9 > 5:
    print(f'A nota do aluno {nome} é de {m} está na média mas necessita de \033[1:34mRECUPERAÇÃO!\033[m')
elif m > 7.0:
    print(f'A nota do aluno {nome} é de {m} uma otima nota o aluno está \033[1:32mAPROVADO!\033[m')