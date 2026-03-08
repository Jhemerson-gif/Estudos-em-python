from random import randint
computador = randint(0,3)
print('-=-'*20)
print('Sou seu computador ... Acabei de pensar em um número entre 0 e 10')
print('Será que vocÊ conseuge adivinhar qual foi?')
print('-=-'*20)
acertou = False
tentativas = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite?').strip())
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais ..., tente novamente:')
        elif jogador > computador:
            print('Menos... tente novamente')


print('Você acertou o numero!')
print(f'Você tentou \033[1m{tentativas} vezes \033[m  para acertar!')

