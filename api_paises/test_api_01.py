import requests

pais = input("Digite o nome do país: ")

url = f"https://restcountries.com/v3.1/name/{pais}"

response = requests.get(url)

dados = response.json()

if isinstance(dados, list) and len(dados) > 0:
    pais_info = dados[0]
    nome_pais = pais_info.get("name", {}).get("common", "N/A")
    capital = pais_info.get("capital", ["N/A"])[0]
    regiao = pais_info.get("region", "N/A")
    populacao = pais_info.get("population", "N/A")

    print(f"Nome do país: {nome_pais}")
    print(f"Capital: {capital}")
    print(f"Região: {regiao}")
    print(f"População: {populacao}")