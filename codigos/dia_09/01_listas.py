#List Comprehension
# %%
x = []

# Adicionando valores a lista x
for i in range(1,101):
    x.append(i)
x
# %%
# Usando o for para iterar e juntamente adicionar valores a lista y
# O i alem de iterar, tambem sera um elemento que sera adicionado a lista y
y = [i for i in range(1,101)]
y
# %%
# Usando uma funcao que verifica se o numero é par dentro do for
# Criando uma funcao que sera requisitada no laco for
def par(x):
    return x % 2 == 0

# Podemos tambem utilizar outras formas de validar valores em uma variavel
z = [par(i) for i in range(1,101)]
z
# %%
# Usando uma funcao que mostra somente os numeros pares dentro do for
w = [i for i in range(1,101) if par(i)]
w
# %%
