pessoas = []
temp = []
cont=0
while True:

    nome = input('Digite o nome do aluno: ').title().strip()
    nota1 = float(input(f'Digite a 1• nota: '))
    nota2= float(input(f'Digite a 2• noota:'))
    media = (nota1 + nota2)/2

    temp.append(nome)
    temp.append([nota1,nota2])
    temp.append(media)

    pessoas.append(temp[:])
    temp.clear()


    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break



print('-='*30)

print(f'{'No.':<4}  {'NOME':<10}   {'MÉDIA':>8}')
print('-'*30)
for i, p in enumerate(pessoas):
    print(f'{i:<4} {p[0]:<10} {p[2]:8.1f}')

print('-'*30)
while True:
    opcao= int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if opcao == 999:
        print('Finalizando...')
        break
    if opcao <= len(pessoas)-1:
        print(f'Notas de {pessoas[opcao][0]} são {pessoas[opcao][1]}')


print('<<< VOLTE SEMPRE >>>')
