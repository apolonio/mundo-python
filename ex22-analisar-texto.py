#!/user/bin/env python3
# Autor: Apolonio Santiago Junior
# @apolocomputacao@gmail.com
# Programa que analisa textos 
# Utilização: $python3 ex22-analisar-texto.py

# ASSUNTO: CADEIA DE CARACTERES
'''Crie um programa qe leia o nome compelto de uma pessoa e mostre:
- O nme com todas as letras maiusculas e minusculas
- Quantas letras ao todo
- Quantas letras tem o primeiro nome
'''

nome = str(input("Digite o seu nome completo: ")).strip() 
# funcao strip elimina todos os vazios - espaços antes e depois
# nome.count(' ') # contando os espaços vazios

print("Analisando seu nome!")
print("Seu nome em maiúsculo é {}".format(nome.upper()))
print("Seu nome em minúsculo é {}".format(nome.lower()))
print("Seu nome tem ao todo  {} letras ".format(len(nome) - nome.count(' ')))
print("Seu primeiro nome tem {} letras ".format(nome.find(' ')))

# USANDO FUNCAO SPLIT outra forma de saber o primeiro nome
separa = nome.split()
# Essa funcao pega o nome completo e separa em indices dentro da lista(array)
print("Seu primeiro nome é {} e tem {} letras".format(separa[0], len(separa[0])))
