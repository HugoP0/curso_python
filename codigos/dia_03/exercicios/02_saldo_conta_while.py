saldo_total = 0
saldo=0
while saldo!= "":    
    saldo = input("""
                  (APERTE ENTER SEM ADICIONAR VALOR PARA SOMAR O SALDO)\n
                  Entre com o saldo:
                  """)

    if saldo != "":
            saldo_total += float(saldo)

print("Saldo total: R$",saldo_total)