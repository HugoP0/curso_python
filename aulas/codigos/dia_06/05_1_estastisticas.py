# %%
def soma(a:float,b:float,*args)->float:
    valores = [a,b] + list(args)
    print(valores)
    return sum(valores)

def media (a:float,b:float,*args)->float:
    return soma(a,b,*args) / (len(args)+2)

a = int(input("Digite o valor a"))
b = int(input("Digite o valor b"))
c = int(input("Digite o valor c"))
d = int(input("Digite o valor d"))

print("Soma:",soma(a,b,c,d))
print("Media:",media(a,b,c,d))