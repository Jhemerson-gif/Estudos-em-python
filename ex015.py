a= int(input('Quantos dias o carro foi alugado?'))
k= float(input('Quantos km o Carro pecorreu?'))
dia= 60 * a
km= k * 0.15
t= dia + km

print(f' O Carro alugado por {a:.2f} dias e com {k:.2f} km pecorridos totalizou R${t:.2f}')
