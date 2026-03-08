from itertools import count
from shlex import split

n=str(input("digite seu nome completo: ")).strip()

pn= n.split()

print(n.upper())
print(n.lower())
print(f'O seu nome completo possui', {len(n) - n.count (' ')}, 'letras')
print(f'O seu primeiro nome tem {n.find(' ')} letras')
print(f' O seu primeiro nome é {pn [0] } e possui {len (pn[0]) } letras')

#podendo ser tbm

#n=str(input("digite seu nome completo: "))
#space= n.count(' ')
#print(f'O seu nome completo possui', {len(n)-space}, 'letras')
#print(f' O seu primeiro nome possui {len(n.split()[0])} letras')