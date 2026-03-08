

homem = fem = menor20 = maioridade = 0

while True:

    print('-'*30)
    print(( '     CADASTRE UMA PESSOA'))
    print('-' * 30)
    idade = int(input('Idade:'))
    sexo = ' '
#Condição enquanto de pergunta do sexo
    while sexo not in 'MF' :
        sexo = str(input('Sexo : [M/F])')).upper().strip()

#Condições
        if idade >= 18:
            maioridade += 1
        if sexo == 'M' :
            homem+=1
        if  sexo == 'F' and idade < 20:
            menor20+=1
#Condição enquanto de pergunta  do continuar
    continuar = ' '
    while continuar not in 'SN' :
        continuar= str(input('Quer continuar? [S/N]')).upper().strip()[0]

    if continuar == 'N' :
        break

print('-' * 30)
print(f'Total de pessoas com mais de 18 anos : {maioridade} ')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {menor20} mulheres com menos de 20 anos')




