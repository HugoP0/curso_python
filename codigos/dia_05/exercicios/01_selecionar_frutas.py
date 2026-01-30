fruta = input("Entre com o nome da fruta: ")

frutas_disponiveis= {
    "Pera": "R$ 1.25",
    "Goiaba": "R$ 2.15",
    "Abacaxi": "R$ 3,20",
    "Jaca": "R$ 5.80",
    "Laranja": "R$ 0.65",
    "Limão": "R$ 1,25",
    "Maçã": "R$ 1,50",
    "Banana": "R$ 2,75",
    "Uva": "R$ 1,90"
}


if fruta in frutas_disponiveis:
    print("O valor da",fruta,"é:",frutas_disponiveis[fruta])
else:
    print("Fruta indisponivel ")
