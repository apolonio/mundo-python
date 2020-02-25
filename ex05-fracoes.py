
'''Crie um progrma que leia um numero Real 
qualquer pelo teclado e mostre na tela a sua porcao inteira '''
from math import trunc
num = float(input('Digite um valor: '))
print('O  valor digitado foi {} e a sua porcao inteira é {}'.format(num, trunc(num)))
 
 # Outra forma de faze-lo
 num = float(input('Digite um valor: '))
print('O  valor digitado foi {} e a sua porcao inteira é {}'.format(num, int(num)))
 # UZAMOS A FUNCAO TRUNC importada da biblioteca math ou forçamos o tipo int     