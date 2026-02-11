# %%

txt = "Meu novo arquivo de texto\n"

nome_arquivo = "historia_02.txt"

#Abrindo um arquivo em modo de escrita e adicionando um texto nele
# No modo w, ele ira adicionar o texto sobrescrevendo o que estiver no texto
# O modo a adiciona o texto sem sobrescrever o anterior
with open(nome_arquivo, mode="a") as open_file:
    open_file.write(txt)