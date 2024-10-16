'''
Criando um Gerador de CPF
'''
#########################################
import random
import sys
import re
#########################################

print('GERADOR DE CPF')
entrada = input("Digite quantos CPF's você quer: ")
quantidade_cpf = re.sub(
    r'[^0-9]',
    '',
    entrada
)

#########################################

if quantidade_cpf == '':
    print('Digite algum número.')
    sys.exit()
else:
    int_quantidade_cpf = int(quantidade_cpf)

#########################################

for _ in range(int_quantidade_cpf):
    nove_digitos = ''

    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

#########################################

    contador_regressivo1 = 10

    resultado_digito1 = 0

    for digito in nove_digitos:
        resultado_digito1 += int(digito) * contador_regressivo1
        contador_regressivo1 -= 1

    digito_1 = ((resultado_digito1 * 10) % 11)
    digito_1 = digito_1 if digito_1 <= 9 else 0

#########################################

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo2 = 11

    resultado_digito2 = 0

    for digito_2 in dez_digitos:
        resultado_digito2 += int(digito_2) * contador_regressivo2
        contador_regressivo2 -= 1

    digito_2 = ((resultado_digito2 * 10) % 11)
    digito_2 = digito_2 if digito_2 <= 9 else 0

#########################################

    novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'

    print(novo_cpf)
