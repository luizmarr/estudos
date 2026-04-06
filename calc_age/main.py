# sistema que calcula a idade de uma pessoa com base na data de nascimento e na data atual
from datetime import datetime


class Person:
    def __init__(self, name: str, birth_date: str):
        """Inicializa uma instância da classe Person.
        Args:
            name (str): O nome da pessoa.
            birth_date (str): A data de nascimento da pessoa no formato "YYYY-MM-DD".
        """
        self.name = name
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

    def calculate_age(self) -> int:
        today = datetime.today()
        age = today.year - self.birth_date.year

        # Verifica se o aniversário já ocorreu este ano
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1

        print(f"{person.name} tem {age} anos.")

        return age

    # LUIZ precisa criar um metodo para validar se a data e correta

if __name__ == "__main__":
    name = input("Digite o nome da pessoa: ")
    birth_date = input("Digite a data de nascimento (YYYY-MM-DD): ")

    person = Person(name, birth_date)
    age = person.calculate_age()

    
