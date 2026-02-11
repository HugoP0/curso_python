# %%

A = 1
B = 5

print(A)
print(B)

# %%
C = A
A = B
B = C
print(A)
print(B)
# %%
# Alternando os valores diretamente na variavel
A,B = B,A

print(A)
print(B)
# %%
a,b,*resto = 1,2,3,4,5,6,7
print(a,b,resto)

# %%
a,*resto,b = 1,2,3,4,5,6,7
print(a,b,resto)
# %%

def soma(a, *args):
    total = a + sum(args)
    return total
soma(1,2,3)

# %%
def soma_quatro(a,b,c,d):
    return a+b+c+d

values = [1,2,3,4]
soma(*values)

# %%
dados = {"nome":"hugo","sobrenome":"calvo"}

for i,j in dados.items():
    print(i,j)