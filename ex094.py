rh = {'nome':'',
      'sexo':''
      }
lista=[]
sexo=[]
feminino=[]
cont=soma=wcont=0
velho=velha=None


while True: #Inicio do loop
    rh['nome']=str(input('Digite o nome do jogador: '))
    while True:
        rh['sexo'] = str(input('Digite o seu sexo : [F/M]')).upper().strip()
        if rh['sexo'] =='M' or rh['sexo']== 'F':
            break
        else:
            print('Sexo inválido, tente novamente')

    idade=int(input('Digite sua idade: '))
    soma+=idade
    rh['idade']=idade

    #Adicionando ao dicionario
    lista.append(rh.copy())
    if rh['sexo'] == 'F':
        feminino.append(rh['nome'])
        feminino.append(rh['idade'])
        feminino.append(rh['sexo'])
        wcont+=1

    continuar = str(input('Deseja incluir mais alguma pessoa ? [S/N]')).upper().strip()
    #Condição  de SIM ou NÃO com possibilidade de correção caso erre!
    while continuar in 'SN':
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N')

    if continuar in 'N':
        break


    print('-='*30)
    cont+=1



print('-='*30)

media = soma/len(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A media de idade do grupo é de {media:.1f}anos') #Média  de idade do grupo
print(f'C) LISTA COM TODAS AS MULHERES')
if len(feminino)>0:
    for mulher in range(wcont):
            print(f'   {feminino[0]} tem {feminino[1]} anos')
            feminino.pop(2)
            feminino.pop(1)
            feminino.pop(0)
else:
    print('Não houve mulheres cadastradas.')
print('-='*30)

for pessoa in lista:
    if pessoa['idade'] >= media:
        if velho is None or pessoa['idade'] > velho['idade']:
            velho = pessoa

    if pessoa['idade'] > media and pessoa['sexo'] == 'F':
        if velha is None or pessoa['idade'] > velha['idade']:
            velha = pessoa

print(f'D) Lista das pessoas que  estão acima da média')

if velho:
    print(f'O homem com maior idade')
    print(velho)


if velha:
    print(f'A mulher com maior idade')
    print(velha)



print()
print('São as pessoas com a maior idade  entre os homens e mulheres da média !')
print('FIM')
print()



