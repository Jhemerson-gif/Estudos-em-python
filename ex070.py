print('-'*30)
print('{:^30}'.format(' LOJA SUPER BARATÃO '))
print('-'*30)
totalcompra = mil = baratopreco = 0
barato = ' '
primeiro_produto = True
#Condição de  loop
while True:
    produto= str(input('Nome do produto:')).upper().strip()
    preco = float(input('Preço:'))
    totalcompra += preco
#A contição correta  para verificar o produto mais barato
    '''if cont == 1:
            menor = preco
            barato = produto
        else:
            if preco < menor:
                menor = preco
                barato = produto'''
#Altenativa 2:
    '''if cont == 1 or preço < menor:
            menor = preco
            barato = produto'''

#Verificação

    if primeiro_produto:
        barato = produto
        baratopreco = preco
        primeiro_produto = False
    else:
        if preco < baratopreco:
            baratopreco = preco
            barato = produto

    if preco >= 1000:
        mil+=1
#Condição Resposta para continuar ou não
    continuar = ' '
    while continuar not in 'SN' :
        continuar = str(input('Gostaria de continuar? [S/N]')).upper().strip()[0]

    if continuar == 'N' :
        break

print('-' * 30)
print(f'O total da compra foi R${totalcompra:.2f}')
print(f'Temos {mil} produtos custando mais de R$1000.00')
print(F'O produto mais barato foi {barato.title()} que custa R${baratopreco:.2f}.')
print('{:-^40}'.format(' FIM DO PROGRAMA '))