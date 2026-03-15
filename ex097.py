
def escreva(txt):
    tam = len (txt) + 4
    print('~' * tam )
    print(f'  {txt}')
    print('~' * tam)


escreva('INICIO DO TESTE  DE FUNÇÃO')
vezes = int(input('Quantos vezes deseja escrever? '))

for c in range (vezes):
    escreva(txt = input("Digite uma frase: "))

