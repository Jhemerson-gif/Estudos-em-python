valores = []

while True:
    valor = valores
    valor= (int(input('Digite um valor: ')))

    if valor in valores:
        print('Valor duplicado! Não vou adicionar ...')

    else:
        valores.append(valor)
        print(f'Valor adicionado com sucesso ...')
    continuar = str(input('Deseja Continuar? [S/N]: ')).strip().upper()

    if continuar == 'N':
        break
print('-='*40)
print(f'Você digitou os valores: ',sorted(valores))