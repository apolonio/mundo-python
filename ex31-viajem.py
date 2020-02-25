
#!/bin/bash/env python3
# Ex31
'''
distancia = int(input("Qual foi a distancia percorrida: "))

if distancia <= 200:
    print("O valor da viajem custa  R${:.2f} ".format(distancia * 0.5))
else:
    print("O valor da viajem custa  R${:.2f}".format(distancia * 0.45))
'''

# Poderia ser feito dessa forma em uma unica linha
distancia = int(input("Qual foi a distancia percorrida: "))
preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print("O valor da viajem custa  R${:.2f} ".format(distancia * 0.5))

