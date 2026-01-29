#O While é adequado para comparacoes logicas e que o laco seja repetido com base em uma condicao logica
#Quais numeros divisiveis por X no intervalo [Y]

count = 4

while count <= 100:
    resto = count % 4
    if resto == 0:
        print(count)
    
    count += 1
