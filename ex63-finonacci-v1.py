#!/user/bin/env python3
# Autor: Apolonio Santiago Junior
# @apolocomputacao@gmail.com
# Programa que calcula fibonacci
# Utilização: $python3 ex63-fibonacci.py

valor = int(input("Digite um valor para Calcular Fibonacci: "))

ant = atual = prox =  1
cont = 0
print(f'Calculando Fibo {valor} = {atual} - ',end ='')
while cont < valor:
    print(f'{prox}', end=' ')
    print(" - " if cont < valor else  " = ", end=' ')
    prox = ant + atual
    ant = atual
    atual = prox
    cont +=1