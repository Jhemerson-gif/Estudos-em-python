times = [('Botafoto',  63), ('Palmeiras', 76), ('Fortaleza', 43), ('Internacional', 44), ('Flamengo', 79),('São Paulo', 51),  ('Cruzeiro', 70),
         ('Bahia', 60), ('Corinthians', 47), ('Vitória', 45), ('Vasco', 45), ('Juventude', 35),('Grêmio', 49), ('Fluminense', 64), ('Atlético-MG', 48) ,('RB Bragantino', 48),('Sport', 17),('Mirassol', 67),('Ceará', 43)]




print('-='*100)
print(f'Lista de  times do brasileirão: {times}')
print('-='*100)

print(f'Os 5 primeiros colocados {(times[5])} ')
print('-='*100)
print(f'Os 4 últimos colocados {times [-4:]} ')
print('-='*100)
nomes = [t[0]for t in times]
posicao = nomes.index("São Paulo")
print(f'Times em ordem alfabética: {sorted(times)}')

print(f'A Chapecoense não está dispultando o campeonato  mas você tem o São paulo  que está na {posicao} posição  da lista !')