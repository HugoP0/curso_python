texto = """"
Escolha a sua água para comprar
1. Agua mineral natural R$ 1.50
2. Agua mineral com gas R$ 2.50
"""
opcao = input(texto)

valor_item=0

if opcao == "1":
    valor_item = 1.5
elif opcao == "2":
    valor_item = 2.5

if valor_item == 0:
    print("Opção inválida. Coloque a opção certa, porra ! Com todo respeito :D")
else:
    qtde_garrafas= input("Quantas garrafas você deseja? ")
    valor_total = valor_item * int(qtde_garrafas)
    print("Sua conta ficou: R$",valor_total)