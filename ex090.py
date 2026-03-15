aluno = {'nome':'',
         'media':0

}

aluno['nome']= str(input('Digite o nome do aluno: ')).title()
aluno['media']= float(input('Digite a média do aluno: '))

print(f'Nome  é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
print('-='*20)
listajogadores = []

if aluno['media'] >= 7:
    aluno['situacao']= 'Aprovado'
elif 5 <= aluno['media'] <7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'  -{k} é igual a {v}')
print(aluno)

'''
if aluno['media'] <= 4.9:
    print(f'O aluno {aluno["nome"]} está REPROVADO')
elif aluno['media'] > 5 and aluno['media']<= 6.9:
    print(f'O aluno {aluno["nome"]} está em RECUPERAÇÃO')
else:
    print(f'O aluno {aluno["nome"]} está APROVADO !')'''