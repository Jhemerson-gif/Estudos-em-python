n= cont = total = 0
parar = 999
n= int(input('Digite um numero [999 para parar]:'))
while n != parar:
    total += n
    cont += 1
    n = int(input('Digite um numero [999 para parar]:'))

print(f'Você digitou {cont} números e a soma entre eles foi {total}')