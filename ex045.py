import time
import random
print(f'Prepara-se seu perdedor vamos jogar jokenpô!')
regra= input(f'Você conhece as regras do jokenpô?').lower()

op= ['pedra', 'papel', 'tesoura']

#regras

if regra == 'não':
    print(f'Jokenpô é um jogo onde temos as opções \033[:31mPedra, Papel\033[m ou \033[:31mTesoura\033[m, onde \033[:31mPedra vence Tesoura\033[m mas perde para \033[:31mPapel\033[m, seguindo assim consecultivamente!')
    pronto=input(f'Você está pronto para jogar ?')
elif regra == 'sim':
    print(f'Ok, Vamos continuar !')

#jogo

jogador=input(f'Ok, então vamos começar! \n\033[:1mPedra, Papel ou Tesoura!\033[m').strip().lower()

if jogador not in op:
    print(f'Escolha invalida tente novamente!')

print("\033[:1:31mJO...\033[m")
time.sleep(0.5)
print("\033[:1:31mKEN...\033[m")
time.sleep(0.5)
print("\033[:1:31mPO!!!\033[m")
time.sleep(0.5)


computador= random.choice(op)

if jogador in op:
    print(f' Eu Escolho \033[:1:31m{computador}\033[m')

print('Processando...')
time.sleep(2)


if jogador == computador:
       print(f'\033[:1mEmpate!\033[m')
elif (jogador =='pedra' and computador=='tesoura') or (jogador == 'tesoura' and computador == 'papel') or (jogador == 'papel' and computador == 'pedra'):
    print(f'\033[:1:33mParabens vocÊ venceu dessa vez !\033[m')
else:
    print('\033[:1:34mHaha, Você perdeu !\033[m')

