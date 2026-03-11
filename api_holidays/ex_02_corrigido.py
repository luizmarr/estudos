import json
import requests


def get_input():
    year = input("Digite o ano para consultar os feriados: ")
    country_code = input("Digite o código do país (ex: BR para Brasil): ")
    return year, country_code


def get_holidays(year: str, country_code: str):
    """
    Consulta os feriados públicos de um país para um determinado ano usando a API do Nager.Date.
    Args:
        year (str): O ano para o qual os feriados devem ser consultados.
        country_code (str): O código do país (ex: BR para Brasil).
    Returns:
        list: Uma lista de dicionários contendo informações sobre os feriados, incluindo a data,
              o nome local e o nome em inglês.
    """
    url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country_code}"
    response = requests.get(url=url, verify=False)
    data = json.loads(response.content.decode("utf-8"))
    return data


def extrair_dados_feriado(holiday: dict):
    '''Extrai a data, o nome local e o nome em inglês de um dicionário de feriado.'''
    date = holiday['date']
    local_name = holiday['localName']
    name = holiday['name']
    return date, local_name, name


def print_country(year: str, country_code: str):
    '''Imprime o nome do país e o ano para os quais os feriados estão sendo consultados.'''
    print(f"\nFeriados em {country_code} para o ano de {year}:")


def print_holiday(date: str, local_name: str, name: str):
    '''imprime as infirmaçoes do feriado'''
    print(f"{date}: {local_name} ({name})")


def main(year: str, country_code: str):
    data = get_holidays(year, country_code)

    print_country(year, country_code)

    for holiday in data:
        # FALTOU COLOCAR O PRINT_HOLIDAY AQUI DENTRO DO FOR PARA IMPRIMIR CADA FERIADO
        date, local_name, name = extrair_dados_feriado(holiday)
        print_holiday(date, local_name, name)


if __name__ == "__main__":
    # year, country_code = get_input()
    year = "2026"
    country_code_list = ["BR", "US", "DE", "FR", "IT"]
    for country_code in country_code_list:
        main(year, country_code)
