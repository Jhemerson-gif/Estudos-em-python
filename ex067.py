cont = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor?'))

    print('-' * 40)
    if n <= 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        print('-' * 40)
        break

    for c in range(1, 11):
        cont += 1
        mult = n*c
        print(f'{n} x {c} = {mult} ')




    print('-' * 20)
