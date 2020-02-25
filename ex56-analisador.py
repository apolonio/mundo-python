"""
DESAFIO 056: Analisador Completo
Desenvolva um programa que leia o nome, idade e sexo de 3 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""
total = 0
idade_idoso = 0
nome_idoso = ''
garotas = 0
for c in range(1, 3 + 1):
    valor1 = ('Digite o nome da pessoa  {} (ex: Rondon): '.format(c))
    valor2 = ('Digite a idade da pessoa  {} (ex: 30): '.format(c))
    valor3 = ('Digite o sexo da pessoa  {} [M/F]: '.format(c))
    nome = str(input(valor1)).strip()
    idade = int(input(valor2))
    sexo = str(input(valor3)).strip().upper()
    print()
    total += idade
    if idade > idade_idoso and sexo in 'Mm':
        idade_idoso = idade
        nome_idoso = nome
    if idade < 20 and sexo in 'Ff':
        garotas += 1

media = int(total / 4)
print('A média de idade do grupo é {} anos.'.format(media))

if nome_idoso == '':
    print('Não tem nenhum homem no grupo.')
else:
    print('O homem mais velho do grupo tem {} anos e se chama {}.'.format(idade_idoso, nome_idoso))

if garotas == 0:
    print('Não tem nenhuma mulher com menos de 20 anos no grupo.')
elif garotas == 1:
    print('Tem somente uma mulher com menos de 20 anos no grupo.')
else:
    print('Tem {} mulheres com menos de 20 anos no grupo.'.format(garotas))