lista_pessoas=[]
soma = 0
#Leitura dos dados !
while True:
    lista = {}
    lista['nome'] = str(input('Nome: '))
    idade = int(input('Idade: '))
    soma+= idade

    lista['idade'] = idade

    while True: #Validação sexo
        lista['sexo'] = str(input('Sexo: ')).upper().strip()[0]
        if lista['sexo'] in  'MF':
            break
        print(f'Erro! Por favor, digite apenas M ou F')

    lista_pessoas.append(lista.copy())



    while True:#Validação de Continuação
        continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Erro! Por favor, digite apenas S OU N')

    if continuar == 'N':
        break
#Resultado analisado

media =  soma/ len(lista_pessoas) #Média  de idade do grupo

print(lista_pessoas)
print(f'A) Ao todo temos {len(lista_pessoas)} pessoas cadastradas.')
print(f'B) A  média de idade é de {media:.1f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in lista_pessoas: #Validação de mulheres cadastradas
    if str(p['sexo']) in 'F':
        print(f'{p["nome"] }', end='')
print()


print(f'D) Lista das pessoas que estão acima da média:')
for p in lista_pessoas:  #Validação de pessoas acima da média de idade
    if p['idade'] >= media:
        print(f'    ', end='')
        for k,v in p.items():
            print(f'{k} = {v}; ', end='')
        print()

print('FIM DO PROGRAMA !')