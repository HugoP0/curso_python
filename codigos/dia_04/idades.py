# %%
#Mostrando como listas sao objetos mutaveis
idades = []

while True:
    idade = input("Entre com a idade:")

    if idade == "":
        break
    
    idades.append(int(idade))

print("Lista de idades adicionadas: ",idades)

media = sum(idades)/ len(idades) 
minimo = min(idades) 
maximo = max(idades) 
qtde_idades= len(idades) 

print("MEDIA: ",media)
print("MINIMO: ",minimo)
print("MAXIMO: ",maximo)
print("QTDE_IDADES: ",qtde_idades)