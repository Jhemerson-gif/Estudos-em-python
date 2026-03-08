'''v=float(input('\033[2:35:40m' 'Digite a distancia que indicaremos o preço :\033[m'))'''

#Método 1
'''if v <=200:
    c= v* 0.50
    print(f'O valor da viagem será de R$\033[2:31m{c}\033[m, considerada uma viagem curta !')
else:
    c2= v* 0.45
    print(f'O valor da viagem é de R$\033[2:31m{c2}\033[m, considerada uma viagem longa !')'''

#Método 2

distancia= float(input('\033[2:35:40m' 'Digite a distancia que indicaremos o preço :\033[m'))
print(f'Você está prestes a começar uma viagem de \033[2:31m{distancia}\033[m km')
preco= distancia * 0.50 if distancia <=200 else distancia * 0.45
print(f'E o preço da sua passagem será de \033[2:31mR$ {preco:.2f}\033[m')