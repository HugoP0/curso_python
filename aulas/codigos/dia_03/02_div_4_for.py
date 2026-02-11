#O laço for é apropiado para percorrer um objeto
#Quais numeros divisiveis por X no intervalo [Y]

x= input("Digite um número para descobrir seus divisores exatos (Resto 0): ")
y= int(input("Agora, digite qual intervalo de números que deseja para apresentar os divisores exatos: "))

for i in range(y+1):
    if i % float(x) == 0 and i >= 1:
        print("O número",x,"é um divisor exato com o número:", i)