numero = 'zero', 'um', 'dois', 'tres', 'quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','cartoze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'

while True:
    num= int(input('Digite um número entre 0 e 20: '))
    if num > 20:
        print('Tente novamente.')
    else:
        print(f'Você digitou o numero {numero[num].title()} !')
        break