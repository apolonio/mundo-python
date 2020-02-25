48 - Mostra os numeros pares de 1 ate 50
# Desafio 48 - Números Pares
print ('Número Pares de 1 a 50!!!')
for c in range (1, 51):
    if c % 2 == 0:
        print (c)
print ('FIM!')

49 -  Mostar a tabuada de numero usando laço for

n = int(input('Qual numero deseja ver a tabuada? '))
for c in range(1, 11, 1):

    print('{} x {} = {}'.format(n, c, n*c))

print('fim')


50 - Leia 6 numeros inteiros e mostre a soma apenas dos pares. Se o valor for impar desconsidere
51 - Ler o primeiro termo e a razao de uma PA, Mostre os 10 primeiros termos da PA.

termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
for i in range(termo, decimo + razao, razao):
    print(i)
    
52 - Leia um numero e diga se ele é PRIMO
53 - Leia uma frase e diga se é um PALINDROMO
      apos a sopa - subi no onibus - a sacada da casa - a torre da derrota - o lobo ama o bolo - anotaram a data da maratona
54 - Leia o ano de nascimento de 7 pessoas e mostre quantos sao maiores de 21 anos.
55 - Leia o peso de cinco pessoas e diga qual o maior e o menor peso

peso = []
for i in range(0, 5):
        peso.append(float(input('informe o peso: ')))
print('O menor peso informado foi: {} é o maior peso informado foi {}'.format(min(peso), max(peso)))

56 - Leia nome, idade e sexo de 4 pessoas e no final:
    - A media de idade do grupo
    - Qual é o nome do grupo Homem mais velho
    - Quantas mulheres tem menos de 20 anos
    
57 - Validacao de Dados 

66 - Calcula a soma
67 - Calcular a tabuada e encerrar quando for negativo
68 - Faça um programa que jogue par ou impar e calcule a some e mostre o numero de vitorias
69 - Leia o sexo e a idade de varias pessoas 
    - Quantas mulheres tem menos de 20 anos
    - Quantos homens foram cadastrados
    - Pessoas com mais de 18 anos
70 - Leia o nome e o preco de varios produtos. Pergunte se deseja continuar e no final:
   - Total gasto
   - quantos produtos custam mais de 1000
   - Qual é o nome do produto mais barato

71 - Realizando saques em um caixa eletronico, considerando que o programa possui cédulas de 50, 20 ,10,1! 
   - Mostre a quantidade de cada célula.