# %%

#Uma maneira de definir listas
# Listas no python nao sao arrays
idades= [28,42,43,35,39,28,38,26,48,26]

# Soma idades
print("Soma idades:", sum(idades))
# Qtd idades
print("Qtde idades: ",len(idades))
# Media idades
print("Media idades: ", sum(idades)/len(idades))
#Menor idade
print("Menor idade: ",min(idades))
# %%

hugo = ["Hugo","Calvo",28,False,"Solteiro",128.88]

#Printando conteudos da lista
print(hugo)

#Tipo de lista
type(hugo)

#Printando uma posicao na lista
print(hugo[1])
# %%

#Lista dentro de lista
hugo = ["Hugo Calvo",
        28,
        False,
        "Solteiro",
        ["estagio","assistente","analista"],
        [2000,2100,2300],
        ["kkkkk1","kkkkk2","kkkkk3"] ]

print("Tamanho da lista: ",len(hugo))

#Acessando uma lista dentro de outra lista hard coded
print(hugo[6][2])

#Acessando uma lista definindo posicoes com funçoes

tamanho = len(hugo)
pos = tamanho - 1

risadas = hugo[pos]
print(hugo[pos][0])

hugo[pos][len(risadas)-1]

# %%
hugo[-1][-2]

# %%
# Primeiro 4 elementos de ums lista 
hugo[:4]

# %%
hugo[4][1:]
# %%
# Os ultimos elementos de uma lista
hugo[4][-2:]

# O start e stop definem por onde começar e terminar.
# hugo[start : stop]
# Caso você oculte o start você irá iniciar pelo começo da lista
# Caso você ocultar o stop, você irá até o final da lista

# Navegar na lista de trás para frente
# %%
salarios = hugo[5]
salarios[::-1]

# hugo[start, stop, step]
# %%