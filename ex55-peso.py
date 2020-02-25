# 55 - Leia o peso de cinco pessoas e diga qual o maior e o menor peso

peso = []
for i in range(0, 5):
        peso.append(float(input('informe o peso: ')))
print('O menor peso informado foi: {} é o maior peso informado foi {}'.format(min(peso), max(peso)))