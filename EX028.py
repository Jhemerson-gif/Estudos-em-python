import random
import time
from time import sleep

print('-=-'*20)

n= int(input('Digite um numero e tente adivinhar: '))
print('-=-'*20)

print('PROCESSANDO...')
sleep(3) # tempo de derlay do processando

import random
c= random.randint(1,5) # Escolha randomizada de numero

if n == c:
    print(f'Você acertou, eu pensei em {c}!')
else:
    print(f'Você errou tente novamente, eu pensei em {c}!')



