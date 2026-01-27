texto = """"
Escolha a sua água para comprar
1. Agua mineral natural
2. Agua mineral com gas
"""
opcao = input(texto)
conta=0

if opcao == "1":
    conta = 1.5
elif opcao == "2":
    conta = 2.5

if conta == 0:
    print("Opção inválida. Coloque a opção certa, porra ! Com todo respeito :D")
else:
    print("Sua conta é: R$",conta)