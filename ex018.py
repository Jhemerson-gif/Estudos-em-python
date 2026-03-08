from math import radians , sin, cos, tan
a= float(input('Digite o valor do angulo:'))

s= sin(radians(a))
c= cos(radians(a))
t= tan(radians(a))

print(f'O ângulo de {a} tem seno de {s:.2f}\n O ângulo de {a} tem o COSSENO de {c:.2f}\n O ângulo de {a}tem a tangente de {t:.2f}')