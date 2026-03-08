from time import sleep

print('\033[1:31mPrepara-se para a contagem regressiva pois vai estourar os fogos !\033[m')
for c in range (10, -1, -1):
    print(f'\033[1:31m {c}\033[m')
    sleep(1)

print('\033[1:31mFeliz Ano Novo !!!\033[m')