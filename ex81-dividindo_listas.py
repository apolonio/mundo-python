#!/user/bin/env python3
# Autor: Apolonio Santiago Junior 
# @apolocomputacao@gmail.com

'''
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
 respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''

valores = list()
par = list()
impar = list()
while True:
    # Detalhe na forma como capturar com append direto na lista
    valores.append(int(input('Digite um valor: ')))     
    resp=str(input('Deseja continuar:[S|N] ')).strip().upper()
    if resp in 'N':
        break
# DEPOIS DE SAIR DO WHILE é hora de analisar a lista
for i, v in enumerate(valores): 
    if v % 2 == 0:
         par.append(v)    
    elif v % 2 == 1:
        impar.append(v) 
print('-='* 30)
print(f'Lista completa:  {valores}')
valores.sort()
print(f'Lista Ordenada:  {valores}')
print(f'Lista par:  {par}')
print(f'Lista impar:  {impar}')


    