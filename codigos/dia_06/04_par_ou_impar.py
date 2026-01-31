# %% 
def par_impar(numero:int):
    if numero % 2 == 0:
        print(numero, "é par")
    else:
        print(numero,"é impar")

numero = int(input("Entre com um numero: "))

par_impar(numero)