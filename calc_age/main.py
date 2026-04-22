# sistema que calcula a idade de uma pessoa com base na data de nascimento e na data atual
from datetime import datetime


class Person:
    def __init__(self, name: str, birth_date: str):
        """Inicializa uma instância da classe Person.
        Args:
            name (str): O nome da pessoa.
            birth_date (str): A data de nascimento da pessoa no formato "YYYY-MM-DD".
        """
        formatos_validos = ["%Y-%m-%d", "%y-%m-%d"]
        self.name = name
        self.birth_date = None

        for formato in formatos_validos:
            try:
                self.birth_date = datetime.strptime(birth_date, formato)
                break
            except ValueError:
                continue
        raise ValueError("Data de nascimento inválida.")

    def calculate_age(self) -> int:
        today = datetime.today()
        age = today.year - self.birth_date.year

        # Verifica se o aniversário já ocorreu este ano
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1

        print(f"{self.name} tem {age} anos.")

    def validate_date(date_str: str) -> bool:
        """Valida se a data fornecida está no formato correto e é uma data válida.
        Args:
            date_str (str): A data a ser validada no formato "YYYY-MM-DD".
        Returns:
            bool: True se a data for válida, False caso contrário.
        """
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

  
    # aceitar ano com dois digitos e com quatro digitos

if __name__ == "__main__":
    name = input("Digite o nome da pessoa: ")

    while True:
        birth_date = input("Digite a data de nascimento (YYYY-MM-DD ou YY-MM-DD): ")
        if Person.validate_date(birth_date):
            break
        else:
            print("Data de nascimento inválida. Por favor, tente novamente.")
    birth_date = input("Digite a data de nascimento: ")

    

    
