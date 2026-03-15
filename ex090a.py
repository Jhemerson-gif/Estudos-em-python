

listaalunos = []
while True:
    alunos={} #Testando com dicionario vazio

    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    alunos['nome']= nome
    alunos['media'] = media
    alunos['nota1']= nota1
    alunos['nota2']= nota2


    #Situação do aluno
    if media >=7:
        alunos['situacao'] = 'Aprovado'
    elif media < 7 and media >=5:
        alunos['situacao']= 'Recuperação'
    else:
        alunos['situacao'] = 'Reprovado'

    #Copiando lista de alunos a cada loop
    listaalunos.append(alunos.copy())



    conitnuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if conitnuar == 'N':
        break

print('-='*40)

for a in listaalunos:
    print(f'O aluno {a["nome"]} teve média {a["media"]} .')
    print(f'O aluno está {a["situacao"]} !')
print('-='*40)
