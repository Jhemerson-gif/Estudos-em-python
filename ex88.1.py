from random import randint
from time import sleep
tot=0
print('-'*30)
print('JOGA NA MEGA SEGA'.center(30))
print('-'*30)
sorteio=int(input(f'Quantas vezes deseja sortear? '))
print('-='*3,f'SORTEANDO {sorteio} jogos','-='*3)
lista=[]
while tot <= sorteio -1:
    tot+=1
    lista = list()
    cont=0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >= 6:
            break
    lista.sort()
    print(f'Jogo {tot}:{lista}')
    sleep(1)
print('-='*4,'< BOA SORTE >','-='*4)