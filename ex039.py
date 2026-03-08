from datetime import date
print(f'\033[:1:2m Ola bem vindo ao Portal do Exercito Brasileiro! \n Digite a baixo para descobrir sua situação!\033[m')

nome= (input('Digite o seu nome:').title())
data= int(input('Digite o ano do seu nascimento:'))
sexo= input('Digite o seu sexo: Masculino/Feminino')
atual = date.today().year
tempo= atual - data


if sexo == 'feminino':
    print(f'{nome} não existe obrigatoriedade para alistamento femino, caso queira se alistar me diga se sim ou não!')
    deseja= (input('VocÊ deseja servir o exercito ?:').lower().strip())
    if deseja == 'sim':
        print('Ok, então vamos continua')
    elif deseja =='não':
        print('Entendo  tenha um otimo dia !')
    else :
        print('Opção invalida tente novamente !')

elif sexo == 'masculino':
    print(f'{nome} vamos dar continuidade no formulario !')
else:
    print('Sexo invalido. digite novamente "masculino" or "feminino"')




print(f'Quem nasceu em {data} tem {tempo} anos em {atual}.')


if tempo == 18:
    print(f'{nome} você está na apto para o alistamento você tem  {tempo} anos, você deve comparecer ao quartel mais proximo de sua casa !')
elif tempo <18:
    saldo= 18 - tempo
    print(f'{nome} a idade minima para o alistamento é de \033[:31m18 anos\033[m dentro de {saldo} anos você deve comparecer para o alistamento obrigatorio !')

    ano= atual+saldo
    print(f' O ano do seu alistamento deveria será em {ano}')


elif tempo > 18 and tempo < 45:
    saldo = tempo - 18
    print(f'{nome} Você já deveria ter ser alistado a {saldo} anos')
    ano= atual-saldo
    print(f'Seu ano de alistamento foi de {ano}')

elif tempo >= 45:
    print(f'{nome} você está acima da idade limite de 45 anos !')
