
valor = int(input('Qual tabuada voce deseja calcular: '))


'''Programa que calcula a tabuada de um valor passado pelo usuário '''
for i in range(1,11,1):
    print("{} x {} = {}".format(i,valor,i*valor))