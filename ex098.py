from time import sleep
def contagem():
    #Contagem de 1 a 10
    texto=str('Contagem de 1 até  10 de 1 em 1')
    print('-' * 40)

    print(texto)



    for a in range(1,11):
        print(f'{a}', end=' ')
        sleep(0.5)
        a += 1
    print('FIM!')


    #Contagem de 0 a 10 , 2 em 2
    texto2 = str('Contagem  de 10 até 0 de 2 em 2')
    print('-'*40)
    print(texto2)

    for b in range(0,10,2):


        print(f'{b}', end=' ')
        sleep(0.5)
        b+=1
    print('FIM!')
    print('-'*40)

    #Contagem  por requisição
    print('Agora é sua  vez de personalizar a contagem!')
    i = int(input('Inicio: '))
    f= int(input('Fim: '))
    p = int(input('Passo: '))

    print('-'*40)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    for c in range(i,f+1,p):
        print(f'{c}', end=' ')
        sleep(0.5)
    print('FIM!')







contagem()