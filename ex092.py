documentos = {'nome':'',
              'idade':0,
              'ctps'
              'cpf':'',
              'salario':0,
              'anodecontratação':0,
}

listadedocumentos=[]
aposentar = 35
while True:
    documentos['nome']= input('Digite o seu nome: ').title()
    documentos['idade']= int(input('Digite o seu ano de nascimento: '))
    documentos['ctps']= int(input('Carteira de trabalho (Se não tem experiência digite: 0): '))
    listadedocumentos.append(documentos['idade'])
    idade = 2026

    if documentos['ctps'] != -1:
        idade -= listadedocumentos [0]

    if documentos['ctps'] == 0:
        break
    else:
        documentos['cpf']= int(input('Digite o seu CPF: '))
        documentos['salario']= int(input('Digite o seu salário mensal: '))
        documentos['anodecontratação']= int(input('Digite o ano da sua contratação: '))

        listadedocumentos.append(documentos['anodecontratação'])

    aposentarar = 2026 - listadedocumentos[1]

    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

    if continuar == 'N':
        break


print('-='*40)
print(documentos)
print(f'O nome tem o valor {documentos["nome"]}')
print(f'A idade tem o valor {idade}')
if documentos['ctps'] != 0:
    print(f'O CPF tem o valor {documentos["cpf"]}')
    print(f'O salario tem o valor {documentos["salario"]}')
    print(f'A aposentadoria tem o valor {aposentarar}')

