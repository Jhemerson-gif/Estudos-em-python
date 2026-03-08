from time import sleep
nome= input('Ola, Qual o seu nome ?')
salario=float(input(f'Ola, {nome} seja bem vindo a nossa linha de crédito, quanto seria o seu salario ?'))
empre= float(input(f'Ok, quanto o Senhor(a) {nome} deseja de emprestimo? '))
parcela = int(input('Quantos anos de parcelamento?'))


print(f'Processando...')

cal= salario*0.3
empa= empre/(parcela*12)


if  empa >= cal:
    print(f'Infelizmente {nome} com o seu sálario atual de {salario}, não se é possível cobrir este emprestimo')

elif empa <= cal:
    print(f'Otimo, o seu emprestimo de {empre} terá um tempo de duração de {parcela} anos em parcelas de {empa}')
    acordo=input(f'Gostaria de Concluir o acordo ?').lower()
    if acordo == 'sim' :
        print(f'Otimo, {nome} seu emprestimo foi aprovado!')
    elif acordo == 'não':
        print(f'Entendo, {nome} podemos tentar outra possibilidade!')

