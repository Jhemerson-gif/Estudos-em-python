from datetime import date
b=int(input('\033[1:35m''Digite um ano se ele é bissexto:,Coloque 0 para analisar o ano atual: \033[m'))

if b ==0:
    b= date.today().year
if (b%4== 0 and b%100 !=0 or b%400==0):
    print(f'O ano de \033[1:31m{b}\033[m é bissexto!')
else:
    print(f'O ano de \033[1:31m{b}\033[m não é bissexto!')