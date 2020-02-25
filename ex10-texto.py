
'''Trabalho com STRINGS '''
frase = ("Curso em Vídeo Python")

uma_letra= frase[9]
# frase.upper(frase) # importar modulo primeiro


print("A letra é: ",frase[9])
print("A letra é: ",frase[9:21:2])
print("A letra é: ",frase[:10])

# frase[9:21]   # pega da letra 9 ate a 21
# frase[9:21:2] # pega da letra 9 ate a 21 e vai pulando de 2 em 2
# frase[9::3]   # pega da letra 9 vai até o final : e vai pulando de 3 em tres
# frase[:10]    # pega do iní cio e  vai até o 10
# frase[10:]    # pega do 10 e vai até o final

# Buscar o parametro na string
# frase.find('Android')
# frase.capitalize()
# frase.title() # Primeira letra da palavra vai para maiúsculo
# frase.strip() ou rstrip ou lstrip para direita e esquerda

# DIVISAO
# SPLIT
frase.split() # Separa as palavras em uma lista palavra por palavra

'-'.join(frase) # Coloca um (-) entre cada caractere da string

print(frase.find("video"))
# retorna -1 pois a palavra video nao existe na string
# python diferencia 

# Vou substituir a palavra Python por PHP
frase = frase.replace('Python','PHP')
print(frase)

