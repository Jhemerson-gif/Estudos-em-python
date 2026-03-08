
alunos = {'nome':'',
          'media':'',
          'nota1':'',
          'nota2':''}

while True:
    cont=0
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    alunos['nome']= nome
    alunos['nota1']= nota1
    alunos['nota2']= nota2
    alunos['media']= media
    cont+=1


    conitnuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if conitnuar == 'N':
        break
print('N')
