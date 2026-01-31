# %%
def soma(a:float, b:float)->float:
    return a+b

def media (a:float, b:float)->float:
    return soma(a,b) / 2

a = int(input("Digite o valor a"))
b = int(input("Digite o valor b"))

print("Soma:",soma(a,b))
print("Media:",media(a,b))