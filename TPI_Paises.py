import csv

def cargar_paises():
    paises = []

    with open("paises.csv", mode = "r", encoding = "utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            pais = {"nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]}
            paises.append(pais)
    return paises

paises = cargar_paises()

for pais in paises:
    print (pais)