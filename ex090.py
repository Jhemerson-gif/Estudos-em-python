aluno = {'nome':'',
         'media':0

}

aluno['nome']= str(input('Digite o nome do aluno: ')).title()
aluno['media']= float(input('Digite a média do aluno: '))

print(f'Nome  é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
if aluno['media'] <= 4.9:
    print(f'O aluno {aluno["nome"]} está REPROVADO')
else:
    print(f'O aluno {aluno["nome"]} está APROVADO !')