# mundo-python
Exercícios resolvidos de python de forma gradual!
# Mundo 1
Nessa fase de codificação do curso Python baseado nas aulas de Gustavo Guanabara
# Exercícios Mundo 1
# Exercícios STRINGS
 22 - Crie um programa que leia o nome completo de uma pessoa e mostre: 
    a) O nome com todas as letras maiusculas
    b) O nome com todas as letras minusculas
    c) Quantas letras ao tendo sem os espaços
    d) Quantas letras tem o primeiro nome
 23 - Faça um programa que leia um numero de 0 - 9999 e mostre na tela cada um dos digitos 
    - separadores unidade, dezena, centena e milhar
 24 - Crie um programa que leia o nome de uma cidade e diga se começa com a cidade "Santo"
 25 - Crie um programa que leia o nome de uma e diga se ela tem "SILVA" no nome
 26 - leia uma Frase e dia Quantas vezes aparece letra aparece
 27 - Diga o Primeiro e o último nome de uma pessoa
 28 - Jogo da adivinhação: Computador pensa no numero entre 0 e 5 e tenho que adivinhar!

from random import randint
from time import sleep
computador = randint(0,5) 
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar....')
print('-=-' * 20)

jogador = int(input('Em que numero eu pensei: ')
print('PROCESSANDO....')

sleep(3)
if jogar == computador:
    print("PARABENS! Voce conseguiu me vencer")
else:
    print('GANHEI! Eu pensei no numero {} e voce pensou no numero {}'.format(computador, jogador))

 29 - Radar Eletronico: Se ultrapassar 80 foi mutado e custa 7 reais por km rodado senao nao mostra nada.

vel = float(input("Qual a velocidade: ?"))

if vel > 80:
    print("Voce excedeu a velocidade que é de 80 km/h ")
    multa = (vel - 80)  * 7 # Somente aquilo que excedeu o limite de 80
    print("Voce deve pagar uma multa de R${:.2f}", format(multa))
print("Dirija com segurança!")


30 - Crie um programa que passado um numo inteiro dizer se é par ou impar.

numero = int(input("Digite um numero: "))
resultado = numero % 2
print("O Resultado foi {}".format(resultado))

 31 - Viajens ate 200km paga por km  0,45 senao paga 0,5
distancia = int(input("Qual foi a distancia percorrida: "))
preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print("O valor da viajem custa  R${:.2f} ".format(distancia * 0.5))

32 - Ano bissexto

from datetime import date
# Essa forma é o padrão que todos ensinam, mas existes excessoes 1700 1900
ano = int(input("Que ano vc deseja analisar, se é bissexto: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano  {} é BISSEXTO!".format(ano))
else:
    print("O ano  {} não é BISSEXTO!".format(ano))
    
33 - Leia tres números e diga o menor, maior e MemoryBIO
34 - Salario ate 1250 aumenta 10 %, senao aumenta 15%
35 - Desenvolva um programa que dado 3 valores ele diz se é possível formar um triângulo!

