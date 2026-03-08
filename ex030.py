num= int(input('\033[35m''Digite um numero e descubra se é Par ou Impar: ''\033[m'))
n= num % 2
if n == 0:
    print(f'Seu numero \033[1:31m{num}\033[m é \033[1:31mPAR\033[m')

else:
    print(f'Seu numero \033[1:31m{num}\033[m é \033[1:31mIMPAR\033[m')