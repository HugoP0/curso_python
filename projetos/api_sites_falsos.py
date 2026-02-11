# %%
import requests
import json

sites = ["https-dyno.com",
            "stermconmmunity.com",
            "sleamcommunityi.ru",
            "steammconmunnity.ru",
            "stearncommunity.net.ru",
            "stemcommuynity.com",
            "steamcommunityprofile.online",
            "tokenmintapace68.vercel.app",
            "login-formulary-hypesquadevents.com",
            "discrod-airdrop.com",
            "signup-hypesquad-official.com"]

url = "https://api.fishfish.gg/v1/domains/{sites}"

dados_sites = []

for i in sites:
    resposta = requests.get(url.format(sites=i))
    if resposta.status_code == 200:
        dados_sites.append(resposta.json())

# %%
site_falso = 0
for site in dados_sites:
    print("Site:",site['name'],
        "\nCategoria:",site['category'])
    if site['category'] == 'phishing':
        print("Não coloque dados sensíveis nesse site !")
        site_falso= site_falso + 1

print("Sua lista de sites possui",site_falso,"sites falsos")
# %%
