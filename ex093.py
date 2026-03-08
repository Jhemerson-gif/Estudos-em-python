totalgols={
    'partidas':0,
    'gols':0,
    'total':0
}
gols=[]
contador=[]
todosgols=[]
cont=0

nome= str(input('Digite o nome do jogador: '))
totalgols['partidas'] = int(input(f'Ola {nome}, Quantas partidas você jogou ?'))
for c in range (totalgols['partidas']):
    cont+=1
    contador.append(cont)
    totalgols['gols'] = int(input(f'Quantos gols você fez na {cont} partida? '))
    gols.append(totalgols['gols'])
    totalgols['total'] += totalgols['gols']
    todosgols.append(totalgols['gols'])

    todosgols.pop(0)
totalgols['media']= totalgols['total'] / totalgols['partidas']
print('-='*30)
print(totalgols)
print('-='*30)
print(f'O jogador {nome} jogou {totalgols['partidas']} partidas.')
print(f'Na {totalgols['partidas']} jogadas ele fez {totalgols["total"]} gols')
for b in range(totalgols['partidas']):
    print(f'Nas {contador[0]} marcou {gols[0]} gols')
    contador[0] += 1
    gols.pop(0)


print(f'A sua média de gols por partida é de {totalgols["media"]} gols')

print('-='*30)
