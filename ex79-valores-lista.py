'''
79 - Crie um propgrama onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista. 
Caso o numero ja exista la dentro, ele nao sera adicionado, No final, serao exibidos todos os valores 
unicos digitados. em ordem crescente.
'''

numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)   
        #adicionando no final da lista
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Nao vou adicionar...!')
    r = str(input('Quer continuar? [S|N]: '))
    # se digitar n sai com o break
    if r in 'Nn':
        break
print('#' * 30)
#ordenando
numeros.sort()
print(f'Voce digitou os valores {numeros}')
