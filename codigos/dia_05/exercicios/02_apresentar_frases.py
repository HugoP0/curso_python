frases = {}

while True:
    frase = input("Digite uma frase: ")
    if frase == "":
        break
    
    if frase not in frases:
        frases[frase] = 1
    else:
        frases[frase] += 1

items = list(frases.items())
items.sort(key=lambda x:x[-1],reverse=True)

for chave,valor in items:
    print("A frase:",chave,"repetiu",valor,"vez(es)")
