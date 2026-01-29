numero = input("Digite o número que deseja a tabuada: ")
max_numero= int((input)("Digite quantas multiplicações você deseja:"))

for i in range(1,max_numero+1):
    print(numero, "X", i, "=", int(numero) * i)