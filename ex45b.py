import time
from random import randint
itens =('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 1 ] Pedra
[ 1 ] Papel
[ 2] Tesoura''')
jogador = int(input('Qual é a sua jogada?'))
print('-='*11)
time.sleep(0.5)
print(f'Computador jogou {itens[computador]}')
time.sleep(0.5)
print(f'Jogador jogou {itens[jogador]}')
print('-='*11)

if computador == 0 : # computador jogou pedra
    if jogador == 1:
        print(f'\033[1;31mComputador venceu usando {itens[computador]}\033[m')
    elif jogador == 0:
        print('\033[1;31mEMPATE\033[m')
    elif jogador == 2:
        print(f'Jogador jogou {itens[computador]}e venceu !')
    else:
        print(f' Jogada invalida !')

elif computador == 1:  # computador jogou papel
    if jogador == 1:
        print('\033[1;31mEMPATE\033[m')
    elif jogador == 2:
        print(f'Computador jogou {itens[computador]}e venceu !')
    elif jogador == 0:
        print('\033[1;31mJOGADOR VENCEU\033[m')
    else:
        print(f' Jogada invalida !')

elif computador == 2 : # computador jogou tesoura
    if jogador == 2:
        print('\033[1;31mEMPATE\033[m')
    elif jogador == 0:
        print(f'Computador jogou {itens[computador]}e venceu !')
    elif jogador == 1:
        print('\033[1;31mJOGADOR VENCEU\033[m')
    else:
        print(f' Jogada invalida !')


