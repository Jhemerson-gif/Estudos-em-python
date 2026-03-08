
print(f'\033[1:31m{ " Bem vindo a Banzai Store " :=^60}\033[m')
print(f'Escolhe entre os produtos da Banzai a venda : Camiseta, Short, Sapato, Bone')

produto=input(f'Digite o produto desejado !')

precos={
'camiseta': 120,
'short': 100,
'sapato': 200,
'bone': 250,
}


if produto not in precos:
    print(f'\033[1:31mProduto inválido!\033[m')

else:
    preco = precos[produto]
    print(f'Otima escolha, a {produto.capitalize()} está R${preco} reais! ')

pagamento=(input(f'\033[1:37mDinheiro / Cheque / Cartão /\033[m').lower().strip())


if  pagamento in ['cheque', 'dinheiro']:
    desconto = preco * 0.10
    total = preco - desconto

    print(f'O pagamento em dinheiro tem desconto de 10%, o valor total é de R${total} reais')


elif pagamento == 'cartao':
    print(f'O pagamento em cartão tem as seguintes opções :')
    print('2x sem juros, 3x a 10x com juros no cartão! ')
    desconto = preco * 0.05
    total2 = preco + desconto

    vezes = int(input(f'Em quantas vezes gostaria de pagar ?'))
    if vezes == 2:
        print(f'O valor do total é de \033[1:31m{preco}\033[m')
    elif vezes >= 3:
        print(f'O valor dividido em {vezes}x é incluido juros totalizando \033[1:31m{total2}\033[m reais.')


