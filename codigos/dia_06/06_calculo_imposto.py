# %%

def calc_imposto(preco:float,tx_base:float, **kwargs):
    imposto = preco * tx_base
    
    for i in kwargs:
        print("Imposto",i,kwargs[i])
        imposto += preco * kwargs[i]

    return imposto

impostos_gerais = {
     "municipio":0.01, 
     "estadual": 0.10,
     "nacional" : 0.20
}

valor_produto = float(input("Digite o valor do produto para calcular seu imposto: "))
imposto = calc_imposto(valor_produto,tx_base=0.03,**impostos_gerais)

print("O valor do imposto é:",imposto)
print("O valor final é",valor_produto+imposto)

