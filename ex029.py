import math
from time import sleep
v= float(input('Digite a velocidade do carro:'))
l=80
km=(v-80)*7.00

sleep(2)
if v >80:
    print(f'Você ultrapassou a velocidade {l} Km/h a sua multa é de R${int (km)}!')
else:
    print(f'Você está dirigindo dentro da velocidade aceitável !')
print('Tenha um bom dia, dirija com segurança !')
