database = []
with open("iris.data", "r") as arquivo:
    for registro in arquivo:
        registro = registro.strip()
        if registro:
            database.append(registro.split(","))

print(database)
