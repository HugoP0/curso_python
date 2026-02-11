# %%
soma = 0

qtde_entradas = 4 

for i in range(qtde_entradas): # range (0,qtde_entradas)
    altura = input("Entre com a altura: ")
    soma += float(altura)
    qtde_entradas -= 1

print("A soma das alturas é: ",soma,"m")
# %%