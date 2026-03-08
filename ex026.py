frase= str(input('Digite uma frase: ')).upper().strip()
a=frase.count('A')
b=frase.find('A')+1
c=frase.rfind('A')+1

print(f'A frase tem {a} letra "A"\nA primeira letra "A" ela começa na posição {b}\nA ultima frase e termina em {c} .')