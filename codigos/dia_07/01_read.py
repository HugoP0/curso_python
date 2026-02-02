# %%
nome_arquivo = "historia.txt"

# O with abre e fecha o arquivo de forma automatica,
# para poder realizar alteracoes e evitar que o arquivo corrompa 
# E evitar que esqueça de fechar o arquivo
with open(nome_arquivo) as open_file:
# Abre o arquivo em formato de leitura
    conteudo = open_file.read()

# Lê os dados do arquivo
print(conteudo)

