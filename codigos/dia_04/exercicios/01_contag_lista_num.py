lista = []
numero=0

while numero!= "":    
    numero = input("Digite um numero para adicionar a lista: ")
    if numero != "":
            lista.append(int(numero))

print(lista)

numero = int(input ("Entre com um numero para descobrir a quantidade na lista: "))

cont = 0

for i in lista:
    if i == numero:
        cont+= 1

print("Qtd de numero(s)",numero,"na lista é:", cont)