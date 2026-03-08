from datetime import date
print(f' \033[:1:34mBem vindo a Confederação Nacional de Natação\033[m')
ano=int(input('Digite o ano do seu nascimento para classificarmos sua categoria!'))
atual= date.today().year
idade= atual - ano

if idade <= 9:
    print(f'{idade} Anos é a categoria \033[:1:34mMIRIM\033[m')
elif idade <= 14 :
    print(f'{idade} Anos é a categoria \033[:1:33mINFANTIL\033[m')
elif idade <= 19:
    print(f'{idade} Anos é a categoria \033[:1:32mJUNIOR\033[m')
elif idade <= 25:
    print(f'{idade} Anos é a categoria \033[:1:31mSÊNIOR\033[m')
elif idade > 25 :
    print(f'{idade} Anos é a categoria \033[1:30mMASTER\033[m')