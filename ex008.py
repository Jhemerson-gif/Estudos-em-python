r= float( input('Ola, me diga quantos metros você quer converter para centimentos e milimetros !'))

km= r/1000
hm= r/100
dam= r/10
dm= r*10
t1= r*100
t2= r*1000


print(f'{r} Metros é equivalento a {km}km Kilometros, {hm}hm hectometro, {dam}dam decâmetro, {dm}dm decímetro, {t1}cm centimentos e em milimetros {t2}mm.')
