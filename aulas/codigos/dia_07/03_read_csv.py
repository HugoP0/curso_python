# %%
arquivo = "data.csv"

with open(arquivo) as open_file:
    lines = open_file.readlines()

for l in lines:
    print(l)
# %%

dados = dict()

# Definindo as chaves do dicionario. 
# Removendo o /n e separando os dados da lines pelo ;
chaves = lines[0].strip("\n").split(";")

for c in chaves:
    dados[c] = []

# %%
#Percorrendo todas as linhas a partir da segunda
for l in lines[1:]:

    # Removendo o /n e separando as strings a partir do ;
    valores = l.strip("\n").split(";")

    # Passando pelas chaves do dicionario e adicionando os valores em sua respectiva chave
    # Percorre o range de valores com a quantidade de valores
    for i in range(len(valores)):

        #Acessando a chave e valor na posicao do indice(i) e adicionando um valor a chave
        dados[chaves[i]].append(valores[i])

# Inicializando uma lista de idades para transforma-las em int
idades = []

# Percorrendo a lista de idades com a lista de idades na variavel dados
for i in dados["idade"]:

    #Adicionando a idade a lista de idades, converendo em int
    idades.append(int(i))

#Realizando a media de idades
media = sum(idades) / len(idades)
media