# %%

import requests #Realiza requisiçoes na web
import json # Tratar json de listas/dicionarios para arquivos json
from tqdm import tqdm # Importando uma biblioteca que mostra o progresso
import pandas as pd # Importando para mostrar dados com o pandas
# %%
# Definindo ceps para exportar para arquivo json e usar na url
ceps =["01519000",
       "13329120",
       "21870370",
       "14400760"]

# Definindo url base
url = "https://viacep.com.br/ws/{cep}/json"

# Definindo uma lista para appendar os dados dos CEPS
dados = []

# Navega na lista de ceps
for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    # Verifica se a requisicao foi valida
    if resposta.status_code == 200:
        #Adiciona os dados do cep a lista de dados
        dados.append(resposta.json())

# %%
dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", sep=";")
# %%

# Abre um arquivo ceps.json, com encoding em utf-8
with open("ceps.json","w", encoding='utf-8') as open_file:
    # Usa a biblioteca json e seu meteodo dump, com os dados coletados a partir do cep
    # acessa o arquivo para realizar a escrita
    # Ignora a tabela ASC II
    # Formata o arquivo 
    json.dump(dados,open_file, ensure_ascii=False,indent=4)