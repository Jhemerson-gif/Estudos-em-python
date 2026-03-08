pessoas= list()
info= list()
pesado=[]
leve=[]
ordemdepeso=[]
while True:
    info.append(str(input("Digite o nome da pessoa: ")))
    info.append(float(input("Digite o peso da pessoa: ")))
    pessoas.append(info[:])
    info.clear()

    continuar= str(input('Deseja continuar ? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
for c in pessoas:
    nome = c[0]
    peso = c[1]


    if peso >= 80:
        pesado.append(nome)
        pesomaior = peso
    else:
        leve.append(nome)
        pesoleve = peso

print(f'{len(pessoas)} pessoas foram cadastradas !')
if peso > 80:
    print(f'O maior peso {pesomaior} {pesado} são as pessoas mais pesadas !')
else:
    print(f'Não existe pessoas mais pesadas!')
print(f'O menor peso {pesoleve} {leve} são as pessoas mais leves!')
