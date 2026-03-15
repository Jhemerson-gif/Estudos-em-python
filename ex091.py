from random import randint
from time import sleep
from operator import itemgetter

maior = cont= 0
#Sroteio  dos numeros do dado
sorteio = {'Jhemerson':randint(1,6),
           'Jonas':randint(1,6),
           'Felipe':randint(1,6),
           'Geovane':randint(1,6),

}
ranking =[]


print(f'VAMOS SORTEIO OS NUMEROS EM UM DADO'.center(60))
print('-='*30)
sleep(0.5)
print(f'3...',end=' '  )
sleep(0.5)
print('2....',end=' ' )
sleep(0.5)
print('1...', end=' ' )
print()
print('-='*30)
print(f'VEJAMOS OS NUMEROS SORTEADOS  NO DADO !'.center(60))
sleep(0.5)
print('-='*30)

print(f'Ranking dos jogadores:')

#Listando os nomes e o numero tirado já definido no dicionario
for k, v in sorteio.items():
    print(f'O {k} tirou o numero {v}')
    sleep(0.3)


print('-='*30)
print('OS VENCES DE DADOS'.center(60))
print('-='*30)
sleep(0.5)

#Rankeando os maiores numeros em ordem
ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}• lugar: {v[0]} com {v[1]}')
    sleep(0.5)
print('-='*30)
print(f'Os numeros sorteados foram {ranking[2]}')
