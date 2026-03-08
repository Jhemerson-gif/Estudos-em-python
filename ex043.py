print(f'Vamos calcular o seu IMC')
peso=float(input('Qual o seu peso?'))
altura=float(input('Qual a sua altura?'))
imc=peso/(altura**2)


if imc < 18.5:
    print('Você está abaixo do peso imc')
    ideal = 18.5 - imc
    print(f'Para alcançar o equilibrio precisa aumentar seu imc em {ideal:.2f}')
elif imc >= 18.5 and imc <= 25:
    print('Você está no peso ideal !')
    ideal = imc - 18.5

elif imc >=25 and imc <= 30:
    print('Você está com sobrepeso')
    ideal = imc - 25
    print(f'(Para alcançar o seu equilibrio precisa diminuir seu imc em {ideal:.2f})')

elif imc >=30 and imc <= 40:
    print('Você está com  obesidade')
    ideal = imc - 30
    print(f'Para alcançar o equilibrio precisa diminuir seu imc em {ideal:.2f}')
elif imc >40:
    print ('Você sofre de obesidade mórbida')
    ideal = imc - 40
    print(f'Para alcançar o equilibrio precisa diminuir seu imc em {ideal:.2f}')