maioridadehomem = 0
nomevelho =''
maioridademulher = 0
nomevelha = ''
soma = 0
cont = 0
totmulher20 = 0
for c in range(1, 5):
    print(f'------ {c} Pessoa ------')
    nome= str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade:'))
    sexo =(input('Digite seu sexo M / F')).upper().strip()
    cont = cont + 1
    soma += idade


    if c == 1 and sexo in 'Mf':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'mM' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'fF' and idade < 20:
        totmulher20 += 1
    if sexo in 'Ff' and idade > 20:
        maioridademulher = idade
        nomevelha = nome



media = soma / 4
print(f'A media de idade do grupo é de {media}')
print(f'Tem {totmulher20} mulheres com menos de 20 anos')
print(f'O Homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'A mulher mais velha tem {maioridademulher} anos e se chama {nomevelha}.')