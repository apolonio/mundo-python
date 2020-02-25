
# Autor: Apolonio Santiago Junior 
# @apolocomputacao@gmail.com
# Versao 1.2
# Foi incluído possibilidade de tratar a letra FfMm e utilizar um if para escrever por extenso


sexo = str(input("Digite seu Sexo: [M/F] ")).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input("Informe o sexo corretamente: [M/F] ")).strip().upper()[0]
if sexo in 'Ff':
    sexo = 'Feminino'
else:
    sexo = 'Masculino'
print("Sexo informado com sucesso!: {}".format(sexo))