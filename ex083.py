lista = []
posi=''
#Minha tentativa mas errada !
'''exp = str(input(f'Digite a expressão: '))

for posi, expressao in  exp:
    if posi[0] in lista == '(' and posi[-1] in lista == ')' :
        print(f'Sua expressão é valida')
    else:
        print(f'Sua expressão não é valida')'''


exp=str(input(f'Digite a expressão: '))
for simb in exp:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print(f'Sua expressão está válida!')
else:
    print(f'Sua expressão não está valida!')
