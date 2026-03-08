print('\033[31m''-=-\033[m'*20)
print('Vamos descobrir se conseguimos criar um triangulo')
print('\033[31m''-=-\033[m'*20)
t=float(input('Digite o primeiro lado:'))
t1=float(input('Digite o segundo lado:'))
t2=float(input('Digite o tercfeiro lado:'))



if t < t1 + t2  and t1 < t+t2  and t2 < t+t1  :
    print(f'Sim, é possivel formar um triangulo')

else:
    print(f'Não é possivel formar um triangulo')
