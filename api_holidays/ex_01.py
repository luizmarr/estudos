import requests
import json

year = input("Digite o ano para consultar os feriados: ")

country_code = input("Digite o código do país (ex: BR para Brasil): ")

url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country_code}"

response = requests.get(url=url, verify=False)

data = json.loads(response.content.decode("utf-8"))

print(f"Feriados em {country_code} para o ano de {year}:")
for holiday in data:
    print(f"{holiday['date']}: {holiday['localName']} ({holiday['name']})")