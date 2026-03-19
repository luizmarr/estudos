import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def validate_year(year: str) -> bool:
    '''Valida se o ano é um número inteiro de 4 dígitos.

    Args:
        year (str): O ano a ser validado.
    Returns:
        bool: True se o ano for válido, False caso contrário.
    '''
    return year.isdigit() and len(year) == 4


def validate_country_code(country_code: str) -> bool:
    '''Valida se o código do país é válido.

    Args:
        country_code (str): O código do país a ser validado.
    Returns:
        bool: True se o código do país for válido, False caso contrário.
    '''
    country_code_list = ["BR", "US", "DE", "FR", "IT"]
    return country_code in country_code_list


def validate_month(month: str) -> bool:
    '''Valida se o mês é um número inteiro entre 1 e 12.

    Args:
        month (str): O mês a ser validado.
    Returns:
        bool: True se o mês for válido, False caso contrário.
    '''
    if month == "":
        return True  # Permite que o mês seja opcional
    return month.isdigit() and 1 <= int(month) <= 12


def get_input():
    year = input("Digite o ano para consultar os feriados: ")

    while not validate_year(year):
        print("Ano inválido. Por favor, digite um ano válido (4 dígitos).")
        year = input("Digite o ano para consultar os feriados: ")

    country_code = input("Digite o código do país (ex: BR para Brasil): ")

    while not validate_country_code(country_code):
        print("Código do país inválido. Por favor, digite um código de país válido (ex: BR para Brasil).")
        country_code = input("Digite o código do país (ex: BR para Brasil): ")
    month = input(
        "Digite o mês para consultar os feriados (opcional, deixe em branco para todos os meses): ") or "0"
    while not validate_month(month):
        print("Mês inválido. Por favor, digite um mês válido (1-12) ou deixe em branco para todos os meses.")
        month = input(
            "Digite o mês para consultar os feriados (opcional, deixe em branco para todos os meses): ") or "0"

    if month == "":
        month = 0
    else:
        month = int(month)

    return year, country_code, month


def get_holidays(year: str, country_code: str, month: int):
    """
    Consulta os feriados públicos de um país para um determinado ano usando a API do Nager.Date.
    Args:
        year (str): O ano para o qual os feriados devem ser consultados.
        country_code (str): O código do país (ex: BR para Brasil).
        month (str): O mês para o qual os feriados devem ser consultados (opcional).
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
    month = date.split("-")[1]  # Extrai o mês da data (formato YYYY-MM-DD)
    return date, local_name, name


def print_country(year: str, country_code: str, month: int):
    '''Imprime o nome do país e o ano para os quais os feriados estão sendo consultados.'''
    if month:
        print(
            f"\nFeriados em {country_code} para o ano de {year} e o mês de {month}:")
    else:
        print(f"\nFeriados em {country_code} para o ano de {year}:")


def print_holiday(date: str, local_name: str, name: str):
    '''imprime as infirmaçoes do feriado'''
    print(f"{date}: {local_name} ({name})")


def main(year: str, country_code: str, month: int):
    data = get_holidays(year, country_code, month)

    print_country(year, country_code, month)

    for holiday in data:
        date, local_name, name = extrair_dados_feriado(holiday)

        holiday_month = int(date.split("-")[1])

        if month == 0 or holiday_month == month:
            print_holiday(date, local_name, name)


if __name__ == "__main__":
    if __name__ == "__main__":
        year, country_code, month = get_input()
        
        main(year=year, country_code=country_code, month=month)
