import requests



def get_input():
    year = input("Digite o ano para consultar os feriados: ")
    country_code = input("Digite o código do país (ex: BR para Brasil): ")
    month = int(input("Digite o mês de 1 a 12 para consultar os feriados (opcional, deixe em branco para todos os meses): ") or 0)
    return year, country_code, month


def get_holidays(year: str, country_code: str,):
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
    data = response.json()
    return data

def extrair_dados_feriado(holiday: dict):
    '''Extrai a data, o nome local e o nome em inglês de um dicionário de feriado.'''
    date = holiday['date']
    local_name = holiday['localName']
    name = holiday['name']
    return date, local_name, name

def mostrar_feriados_todos_paises(year: str, month: int):
    country_code_list = ["BR", "US", "DE", "FR", "IT"]

    for country_code in country_code_list:
        main(year, country_code, month)

def print_country(year: str, country_code: str, month: int):
    '''Imprime o nome do país e o ano para os quais os feriados estão sendo consultados.'''
    if month:
        print(f"\nFeriados em {country_code} para o ano de {year} e o mês de {month}:")
    else:
        print(f"\nFeriados em {country_code} para o ano de {year}:")

def print_holiday(date: str, local_name: str, name: str):  
    '''imprime as informaçoes do feriado'''
    print(f"{date}: {local_name} ({name})")


def main(year: str, country_code: str, month: int):
    data = get_holidays(year, country_code)

    print_country(year, country_code, month)

    for holiday in data:
        date, local_name, name = extrair_dados_feriado(holiday)

        holiday_month = int(date.split("-")[1])

        if month == 0 or holiday_month == month:
            print_holiday(date, local_name, name)

if __name__ == "__main__":
    year, country_code, month = get_input()
    main(year, country_code, month)

    opcao = input("Digite 1 para consultar um país ou 2 para consultar todos os países: ")

    if opcao == "1":
        main(year, country_code, month)

    elif opcao == "2":
        mostrar_feriados_todos_paises(year, month)

    else:
        print("Opção inválida.")
        