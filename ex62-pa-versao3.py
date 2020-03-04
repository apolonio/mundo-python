#!/user/bin/env python3
# Autor: Apolonio Santiago Junior
# @apolocomputacao@gmail.com
# Programa que calcula a progressao aritmetica versao 2
# Utilização: $python3 ex62-pa-versao3.py

# Acrescentado a possibilidade do usuário continuar gerando progressões
# O programa para se o usuário digitar 0

print("Gerador de PA - Versão 3.0")
print("-="*10)
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão da P.A: '))
cont = 1
total = 0
resp = 10 # Considera o inicio em 10 termos
while resp != 0:
    total += resp # Acumulando o total
    while cont <= total: # pulo gato
        print(f" {termo} ->",end='') # Essa parte end='' permite ser exibido na mesma linha
        termo += razao
        cont += 1
    print("PAUSA")
    resp = int(input("Informe a nova quantidade de termos? "))
print("PA finalizada com {} termos exibidos".format(total))
