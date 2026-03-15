from datetime import datetime
listadedocumentos=[]

while True: #Cadastramento de dados
    documentos={}
    documentos['nome']= input('Digite o seu nome: ').title()
    nasc = int(input('Digite o ano de nascimento: '))
    documentos['idade']= datetime.now().year - nasc

    documentos['ctps']= int(input('Carteira de trabalho (Se não tem experiência digite: 0): '))
    listadedocumentos.append(documentos['idade'])


    if documentos['ctps'] != 0:
        documentos['cpf']= int(input('Digite o seu CPF: '))
        documentos['salario']= int(input('Digite o seu salário mensal: '))
        documentos['anodecontratação']= int(input('Digite o ano da sua contratação: '))
        documentos['aposentadoria'] = documentos["idade"]+((documentos['anodecontratação']+35) - datetime.now().year)

        listadedocumentos.append(documentos['anodecontratação'])


    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

    if continuar == 'N':
        break


print('-='*40)
print(documentos)
for k, v in documentos.items():
    print(f'{k} tem o valor {v}')
