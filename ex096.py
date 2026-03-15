def cabecario():
    print('-'*30)
    print('CONTROLE DE TERRENOS')
    print('-'*30)

def area(larg,comp):
    a = l * c
    print(f'A area de um terreno {l}x{c} é de  {a}m² ')

cabecario()



l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

area(l,c)
print('-' * 30)