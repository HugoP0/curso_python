lista = [1,2,2,3,3,2,1,1,1,1,1,5,6,7,7,6,5]

numero = int(input ("Entre com um numero: "))

cont = 0

for i in lista:
    if i == numero:
        cont+= 1

print("Qtd de numero(s)",numero,"na lista é:", cont)