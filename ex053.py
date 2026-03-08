d=str(input('Digite uma frase: ')).strip().upper()
palavras = d.split()
junto = ''.join(palavras)
inverso = ''

for c in range(len(junto)-1,-1, -1):
    inverso += junto[c]
print(f'O inverso de {junto} é {inverso}')
if junto == inverso:
     print('A frase digitada  é um palíndromo!')
else:
    print('A frase digitada não é um Palindromo')