from random import randint
v = 0
jogar = ' '
print('-=' * 30)
print(f'\033[1m VAMOS JOGAR PAR OU ÍMPAR\033[m')
print('-='*30)
while True:
    while  jogar not in 'N':
        while True:
            jogador= int(input(f'Digite um numero: '))
            computador = randint(0, 10)
            soma = computador + jogador
            tipo = '  '
            while tipo not in 'PI':
                tipo = str(input(f'Par ou Impar? [P/I]')).upper().strip()[0]
            print(f'Você jogou {jogador} e o computador jogou {computador}. O total é de {soma} .', end= '')
            print('DEU PAR' if soma % 2 == 0  else 'DEU IMPAR')
            if tipo == 'P':
                if soma % 2 == 0:
                    print(f'Você venceu !')
                    v += 1
                    print('-=' * 30)
                else:
                    print('-=' * 30)
                    print(f'Você perdeu !')
                    break
            if tipo == 'I':
                if soma % 2 == 1:
                    print(f'Você venceu !')
                    v += 1
                    print('-=' * 30)
                else:
                    print('-=' * 30)

                    print('VocÊ perdeu !')
                    break
            print('Vamos jogar novamente...')

        print(f'GAME OVER! Você venceu {v} vezes.')
        break
    jogar = str(input('Você gostaria de Continua ? [S/N]')).upper().strip()[0]
    print('-=' * 30)
    if jogar == 'N':
        print('Ok, me chame quando quiser jogar novamente !')
        break


