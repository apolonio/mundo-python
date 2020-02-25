resp = 'S'
soma = quant = media = maior = menor = 0

while resp in 'Ss':
    num = int(input("Digite um número: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp=str(input("Deseja continuar: [S/N] ")).upper().strip()[0]
media = soma / quant
# Usei o parametro f que é uma implementacao da versao 3.6 que permite escrever a string de forma mais rápido
print(f"Você digitou {quant} números e a média foi {media}")
print(f"O maior valor foi {maior} o menor valor foi {menor}")
    
