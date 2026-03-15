totalgols={
    'partidas':0,
    'total':0
}
gols=[]
contador=[]
todosgols=[]

nome= str(input('Digite o nome do jogador: '))
totalgols['partidas'] = int(input(f'Ola {nome}, Quantas partidas você jogou ?'))
for c in range (0,totalgols['partidas']):
    gols.append(int(input(f'Quantos gols você fez na {c+1} partida? ')))
    (totalgols['gols']) = gols[:]
    totalgols['total'] = sum(gols)




totalgols['media']= totalgols['total'] / totalgols['partidas']
print('-='*30)
print(totalgols)
print('-='*30)
for k,v in totalgols.items():
    print(f' O campo {k} tem o valor {v}')


print('-='*30)
print(f'O jogador {nome} jogou {len(totalgols['gols'])} partidas')
for k,v in enumerate(totalgols['gols']):
    print(f'   => Na {k+1} marcou {v} gols')


print('-='*30)
print(f'Foi um total de {totalgols["total"]} gols')
print(f'A sua média de gols por partida é de {totalgols["media"]} gols')

print('-='*30)
