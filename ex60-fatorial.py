
# CALCULANDO O FATORIAL DE FORMA AUTOMÁTICA COM FUNÇÃO IMPORTADA
'''
from math import factorial

n = int(input("Digite um numero para calcular o fatorial: "))
f = factorial(n)
print(f"O Fatorial de {n} é {f}")
'''


# CALCULANDO O FATORIAL UTILIZANDO WHILE
# https://www.youtube.com/watch?v=9dlBZlkvvxY&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=29
n = int(input("Digite um numero para calcular o fatorial: "))
c = n # uso a variável c como auxilio para ir decrementando ex: 6 5 4 3 2 1
f = 1 # vo acumulando a multiplicacao dos valores
print(f'Calculando {n}! = ', end=' ')
while c > 0:
    print(f'{c}', end=' ')
    print(" x " if c > 1 else  " = ", end=' ')
    f *= c  
    c -= 1
print(f" O fatorial é {f}")  #Usando f de fstring para facitar a escrita  


# CALCULANDO O FATORIAL UTILIZANDO FOR
'''
n = int(input("Digite um numero para calcular o fatorial: "))
c = n # uso a variável c como auxilio para ir decrementando ex: 6 5 4 3 2 1
f = 1 # vo acumulando a multiplicacao dos valores
print(f'Calculando {n}! = ', end=' ')
for c in range(1,n+1):
    print(c, end=' ')
    print(" x " if c >= 1 else  " = ", end=' ')
    f *=c 
    c -= 1
print(f" O fatorial é {f}")  #Usando f de fstring para facitar a escrita  
'''
'''
numero = int(input('Digite um número para obter seu fatorial: '))
fatorial = numero
x = 1
while x < numero:
    fatorial *= x
    x += 1
print(fatorial)
'''