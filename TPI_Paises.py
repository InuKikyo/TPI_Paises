import csv

def cargar_paises():
    paises = []

    try:
        with open("paises.csv", mode = "r", encoding = "utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                paises.append({"nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]})
    except FileNotFoundError:
        print ("Archivo csv no encontrado.")

    return paises
    