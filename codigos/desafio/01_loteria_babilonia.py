# Constura um programa que realiza o sorteio de um numero entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute é maior ou menor que o numero sorteado
# Caso o usuário acerte, dê os parabens

import random

def get_input():

    while True:
        try:
            numero_usuario = int(input("Entre com um numero: "))

        except ValueError as err:
            print("Valor invalido, coloque um intervalo entre 1 e 15")
            continue

        if 1 <= numero_usuario <= 15:
            return numero_usuario

        print("Valor invalido, coloque um intervalo entre 1 e 15")

def check_numbers(sorteio,usuario):

    if sorteio == usuario:
        print("Parabens")
        return True

    elif usuario > sorteio:
        print("Numero maior")
        return False

    else:
        print("Numero menor")
        return False


numero_sorteio = random.randint(1,15)

for i in range(3):

    numero_usuario = get_input()
    if check_numbers(sorteio=numero_sorteio,usuario=numero_usuario):
        break

else:
    print("Suas tentativas acabaram !")