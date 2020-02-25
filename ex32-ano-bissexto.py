#!/bin/bash/env python3

# TRABALHANDO COM CORES DO PADROA ANSI
# \033[0;33;44m
#python/estilo/text/background estilos 0 1 negrito  4 sublinhado  7 inverter
# cores 30 ate 37
# background 40 ate 47

from datetime import date
# Essa forma é o padrão que todos ensinam, mas existes excessoes 1700 1900
ano = int(input("Que ano vc deseja analisar, se é bissexto: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano  {} é BISSEXTO!".format(ano))
else:
    print("O ano  {} não é BISSEXTO!".format(ano))

    