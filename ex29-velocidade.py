vel = float(input("Qual a velocidade: ? "))

if vel > 80:
    print("Voce excedeu a velocidade que é de 80 km/h ")
    multa = (vel - 80)  * 7 # Somente aquilo que excedeu o limite de 80
    print("Voce deve pagar uma multa de R$ {:.2f} ".format(multa))
print("Dirija com segurança!")