
gols=[]
time=[]
partidas=[]
#lEITURA E VALIDAÇAO DE DADOS
while True:
    jogadores = {}
    jogadores.clear()
    gols.clear()

    jogadores['nome']= str(input('Digite o nome do jogador: ')).title()
    tot= int(input(f'Quantas partidas {jogadores['nome']} jogou?'))
    partidas.clear()
    for c in range (tot):
        partidas.append(int(input(f'Quantos gols marcou na partida {c+1}? ')))
    jogadores['gols'] = partidas[:]
    jogadores['total'] = sum(partidas)

    time.append(jogadores.copy())


    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break

#ANALISE DOS DADOS
print('-'*40)
print('cod ', end='')
for i in jogadores.keys(): #Tabela organizada, cabeçario
    print(f'{i:<15} ', end='')

print()

for k,v in enumerate(time): # valores ordenados na tabela
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()
print()



print('-'*40)
while True:
    mostrar = int(input('Mostrar dados do jogador? '))
    if mostrar == 999:
        break
    if mostrar >= len(time):
        print(f'ERROR! Não existe um jogador com codigo {mostrar}.')
    else:
        print(f'-- Levantamento do jogador {time[mostrar]["nome"]}')
        for c,k in enumerate(time[mostrar]["gols"]):
            print(f'    No jogo {c+1}  fez {k} gols')
    print('-'*40)
print('<<< VOLTE SEMPRE >>>')
