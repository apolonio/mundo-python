#!/user/bin/env python3
# Autor: Apolonio Santiago Junior 
# @apolocomputacao@gmail.com
# Utilização: $python3 ex81-lista-decrescente.py

'''
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
'''
lista = []

cont = 0
resp = ''
num = 0
while resp != 'N':
    num = int(input('Digite um Numero: '))
    lista.append(num)
    cont += 1
    resp = str(input('Você deseja continuar: [S|N] ')).strip().upper()[0]
    lista.sort(reverse=True) 
print(f'Voce digitou {len(lista)} elementos!')
print(f'Os elementos em ordem decrescente são: {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado!')
else:
        print('O valor 5 não foi encontrado!')
print('ACABOU')

'''

#OUTRA FORMA DE CRIAR
valores = []
while True:
    # Detalhe na forma como capturar com append direto na lista
    valores.append(int(input('Digite um valor: ')))        
    resp=str(input('Deseja continuar:[S|N] ')).strip().upper()
    if resp in 'N':
        break
print('-='* 30)
print(f'Voce digitou {len(valores)} elementos!')
valores.sort(reverse=True)
print(f'Os elementos em ordem decrescente são: {valores}')
if 5 in valores:
       print('O valor 5 foi encontrado!')
else:
        print('O valor 5 não foi encontrado!')
print('ACABOU')

    