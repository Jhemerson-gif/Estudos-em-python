from random import shuffle, sample


a= 'Jhemerson'
b= 'Lucas'
c= 'Luan'
d= 'Jessica'
e= 'Douglas'
f= 'Longan'
g= 'Illumy'
h= 'Johnson'
i= 'Neymar'
j= 'Luke'
Alunos=([a,b,c,d,e,f,g,h,i,j])
la= sample(Alunos,5)
print(f' Irei realizar o sorteio em ordem de alunos {la}')

alt=str(input('Como pratica altenativa vamos testar \n Digite o primeiro nome:'))
alt1=str(input('Digite o segundo nome:'))
alt2=str(input('Digite o terceiro nome:'))
alt3=str(input('Digite o quarto nome:'))

laa= [alt1, alt2, alt3, alt]
shuffle (laa)
print(f'A ordem dos escolhidos é de ')
print(f' {laa}')