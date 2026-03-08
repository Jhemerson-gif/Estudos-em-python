print('Gostaria que desse um aumento salario de 15% para  !')
fu=input (f'Qual Funcionario ?')
fr= float(input('Quanto ele recebe por mêss ?'))
a= (fr*0.15) # ou fr + (fr * 15/100)
t= fr+a

print(f'O funcionario {fu} Recebe atualmente {fr:.2f} e com o seu aumento salárial o seu novo salário será de {t:.2f} reais!')