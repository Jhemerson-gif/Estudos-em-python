lista=[]



for c in range (1,6):
    valor= int(input('Digite um valor: '))


    if len(lista)==0:
        print('Adicionado ao final da lista...')
        lista.append(valor)
    else:
        pos = 0
        while pos < len(lista) and lista[pos] <= valor:
            pos+=1
        lista.insert(pos,valor)
        print(f'Adicionado na posição {pos} da lista...')



print('-='*40)
print(f'Os valores digitados foram: {lista} da lista...')

