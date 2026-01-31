# Dicionarios sao pares de chave/valor
# %%
dados_hugo = {
    "Sobrenome" : "Calvo",
    "Nome" : "Hugo",
    "Filhos": False,
    "Formacao": ["Ciencias da Computacao", " Seguranca da informacao"],
    "Cargos" : [
        {"nome": "estagio ti", "empresa" : "OPI"},
        {"nome": "Assistente de ti", "empresa" : "OPI"},
        {"nome": "Auxiliar de TI ", "empresa" : "Libbs"}
    ]
}


 #%%
#Apresentando os dados do dicionario
print(dados_hugo)

# Acessando ultimo dado da "Formacao" no dicionario
dados_hugo["Formacao"][-1]

# Acessando a lista de "Cargos" dentro do dicionario <dados_hugo> 
# em seguida, acessa o ultimo cargo e apresentando a empresa da lista do "Cargos" selecionado
dados_hugo["Cargos"][-1]["empresa"]

# Atribuindo uma chave nova ao dicionario
dados_hugo["Estado Civil"] = "Solteiro"
# Apresentando o dado da nova chave
dados_hugo["Estado Civil"]
# %%
#Apresentar as chaves do dicionario
print("Chaves:", dados_hugo.keys())

#Apresentar os valores da chave do dicionario
print("Valores:", dados_hugo.values())

# Listando tuplas, onde a chave fica na primeira posicao e o valor na segunda posicao
print("Items:", dados_hugo.items())
# %%

# Removendo chaves do dicionario (fiz cagada)
# dados_hugo.pop("Estado Civil")

# %%
#Acessando a chave com o for e em seguida apresentando a chave e valor
for i in dados_hugo:
    print(i,"=",dados_hugo[i])
# %%
# Realizando o for onde as duas variaveis recebem sequencialmente a chave e o valor da tupla
# Em seguida, apresenta a chave e o valor  
for chave, valor in dados_hugo.items():
    print(chave, "=", valor)