import random
cont = 0

while True:
    print('=-' * 40)
    print(f'\033[1mVAMOS JOGAR PAR OU ÍMPAR\033[m')
    print('=-' * 40)
    valor= int(input('Digite um valor: '))
    escolha = str(input('Par ou Impar? [P/I]')).upper().strip()
    computador = random.randint(1, 10)
    soma = valor + computador
    cont += 1
    div = soma % 2
    vencer = cont - 1
    if div == 0:
        pi = 'P'
        print(f'Você jogou {valor} e o computador jogou {computador}. O total de {soma} deu PAR')
    else:
        pi = 'I'
        print(f'Você jogou {valor} e o computador jogou {computador}. O total de {soma} deu ÍMPAR')

    if escolha != pi:

        print(f'GAME OVER! Você jogou {cont} partidas e venceu {vencer} vezes.')
        break
    else:
        print('Você venceu! Vamos jogar novamente...')



