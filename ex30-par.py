numero = int(input("Digite um numero: "))
resultado = numero % 2
print("O Resultado da divisão é {}".format(resultado))

if resultado == 0:
    print("O numero  {} é par!".format(numero))
else:
    print("O numero {} é impar".format(numero))
