#!/user/bin/env python3
# Autor: Apolonio Santiago Junior
# @apolocomputacao@gmail.com
# Programa que calcula a progressao aritmetica versao 2
# Utilização: $python3 ex61-pa-versao2.py

print("Gerador de PA - Versão 2.0")
print("-="*10)
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
''' # UTILIZANDO FOR
for i in range(termo, decimo + razao, razao):
    print(i)
    '''
# AGORA UTILIZANDO WHILE

cont =1
while cont <= 10:
    print('{} ->'.format(termo), end='')
    termo += razao
    cont += 1
print("FIM")
