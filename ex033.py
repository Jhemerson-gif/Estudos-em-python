
from time import sleep

print('\033[1:35m''Digite 3 numeros que mostrarei o maior e menor!\033[m')
m=int(input('Digite o primeiro: '))
m1=int(input('Digite o segundo numero'))
m2=int(input('Digite o terceiro numero'))
#verificando quem é o menor
menor = m

if m1<m and m1<m2:
    menor=m1
if m2<m and m2<m1:
    menor=m2
# verifiando quem é o maior
maior = m
if m1>m and m1>m2:
    maior=m1
if m2>m and m2>m1:
    maior=m2
    print(F'O menor valor digitado foi \033[1:31m{menor}\033[m')
    sleep(3)
    print(f'O maior valor digitado foi \033[1:31m{maior}\033[m')



