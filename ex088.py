from random import randint
from time import sleep
jogo=[[],[],[],[],[],[]]
tot=0

print('-'*30)
print('JOGA NA MEGA CENA'.center(30))
print('-'*30)
sorteio =int(input('Quantos jogos você quer que eu sorteie?'))


print('-='*3,' SORTEANDO 5 JOGOS ', '-='*3)
while tot <= sorteio:

    for d in range(6):
        tot += 1
        for c in range(0,sorteio):

        jogo[c].append(randint(1,60))




for c in range(0,sorteio):
    print(f'Jogo {tot}: {jogo[c]}')
    sleep(1)

print('-='*5,' < BOA SORTE! > ','-='*5)