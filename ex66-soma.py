
# TRABALHANDO COM BREAK
n = cont =  s = 0
while True:
    n = int(input('Digite um numero:')) 
    if n == 999:
        break
    cont += 1
    s += n
print("A soma vale {} e voce digitou {} numeros".format(s, cont))
# Usando interpolacao de strings a partir da versao 3.5
print(f"A soma vale {s} e voce digitou {cont} numeros") # python 3.6+
# print(f"A soma vale %s e voce digitou %cont numeros", % s, cont) # python 3.6+