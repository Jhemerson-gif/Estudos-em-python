import random
import time
from time import sleep

computador = random.randint(1, 10)
tentativa = 1
print('-=-'*20)
print('Sou seu computador tente adivinhar  o numero entre 0 e 10')
n= int(input('Digite um numero e tente adivinhar: '))

print('-=-'*20)

print('Processando...')
sleep(3)

while n != computador:
    print(f'Você errou, eu pensei em {computador}, continue tentando !')
    tentativa += 1

    computador = random.randint(1, 10)

    n= int(input('Digite outro  numero : '))
    print('Processando...')
    sleep(1)

if tentativa == 1:
    print(f'Eu pensei em {computador} ')
    print('Parabens você acertou de primeira!')
else:
    print(f'Você acertou, eu pensei em {computador}')
    print(f'Você tentou {tentativa} vezes')

print('-=-'*20)


