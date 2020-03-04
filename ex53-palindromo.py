#!/user/bin/env python3
# Autor: Apolonio Santiago Junior
# @apolocomputacao@gmail.com
# Utilização: $python3 ex53-palindromo.py

'''Exercício Python 053: Crie um programa que leia uma frase
qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
 '''

frase= str(input("Digite uma frase ou palavra: ")).strip().upper()
palavras = frase.split()     # Dividindo as palavras em indices dentro da lista
junto = ''.join(palavras)    # Retirando os espaços
inverso = ''
''' percorrendo a variavel junto de traz para frente e adicionando dentro da variavel inverso
o primeiro -1 desconta do tamanho pois a posição começa em zero.
Percorrendo da ultima até a primeira de uma em uma '''
for letra in range(len(junto) -1, -1,-1):
    inverso += junto[letra]
if inverso == junto:
    print(f" Temos um palíndromo, o inverso de {junto} é {inverso}")
else:
    print(" Não temos um palíndromo")





