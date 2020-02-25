#!/user/bin/env python3
# Autor: Apolonio Santiago Junior
# @apolocomputacao@gmail.com
# Programa que separa unidades de num numero
# Utilização: $python3 ex23-separando-numero.py

# ASSUNTO: CADEIA DE CARACTERES
'''Crie um programa que separa as unidades de um número
'''

numero = int(input("Digite num número de 4 caracteres: "))
print("Analisando seu número!".format(numero))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10


print("Unidade {}".format(u))
print("Dezena {}".format(d))
print("Centena {}".format(c))
print("Milhar {}".format(m))

