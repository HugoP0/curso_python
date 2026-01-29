count = 0
numero = input("Digite o número que deseja a tabuada: ")
max_numero= int((input)("Digite quantas multiplicações você deseja:"))

while count<=max_numero: 
    if count >= 1:
        print(numero, "X", count, "=", int(numero) * count)
    
    count += 1