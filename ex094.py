rh = {'nome':'',
      'sexo':'',
      'idade':0
      }
lista=[]
idade=[]
sexo=[]
feminino=[]
cont=soma=wcont=0


while True:
    rh['nome']=str(input('Digite o nome do jogador: '))
    while True:
        rh['sexo'] = str(input('Digite o seu sexo : [F/M]')).upper().strip()
        if rh['sexo'] =='M' or rh['sexo']== 'F':
            break
        else:
            print('Sexo inválido, tente novamente')

    rh['idade']=int(input('Digite sua idade: '))
    lista.append(rh.copy())
    idade.append(rh['idade'])
    if rh['sexo'] == 'F':
        feminino.append(rh['nome'])
        feminino.append(rh['idade'])
        feminino.append(rh['sexo'])
        wcont+=1


    continuar=str(input('Deseja incluir mais alguma pessoa ? [S/N]')).upper().strip()
    print('-='*30)
    cont+=1
    soma += rh['idade']

    if continuar== 'N':
        break
media = soma/len(lista)

print(f'A media de idade do grupo é de {media:.1f}anos')
print('-='*30)
print(f'LISTA COM TODAS AS MULHERES')
for mulher in range(wcont):
        print(f'{feminino[0]} tem {feminino[1]} anos')
        feminino.pop(2)
        feminino.pop(1)
        feminino.pop(0)
print('-='*30)

for pessoa in lista:
    if pessoa['idade'] > media:
        print(f'{pessoa['nome']}', end=',')
print()
print('São as pessoas com a idade acima da média !')

