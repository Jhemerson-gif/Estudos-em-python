print('\033[31m''-=-\033[m'*20)
print('Vamos descobrir se conseguimos criar um triangulo')
print('\033[31m''-=-\033[m'*20)
t=float(input('Digite o primeiro lado:'))
t1=float(input('Digite o segundo lado:'))
t2=float(input('Digite o tercfeiro lado:'))



if t < t1 + t2  and t1 < t+t2  and t2 < t+t1  :
    print(f'Sim, é possivel formar um triangulo')

    if  t== t1 == t2:        #t == t1 and t2 or t1 == t2 and t or t2 == t1 and t: = também pode ser feito assim
        print(f'Seu triangulo é Equilatero')
    elif t == t1 or t1 == t2 or t2 == t : # também pode ser feito assim t != t1 and t2 != t and t2 != t1:
        print(f'Seu triangulo é  Isósceles')
    else: #t != t1 != t2 != t:  para diferente! ! pode ser usado para diferente
        print(f'Seu triangulo é Escaleno')


else:
    print(f'Não é possivel formar um triangulo')
