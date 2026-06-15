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


#Opcion 1. Mostrar países
def mostrar(paises):
    if not paises:
        print ("No hay países cargados.")
        return
    
    for pais in paises:
        print (f"{pais['nombre']} | " f"Población:{pais['poblacion']} | " f"Superficie:{pais['superficie']}" | f"Continente: {pais['continente']}")





#Menú
def mainmenu():
    print ("\n=====Menú=====")
    print ("1. Mostrar países")
    print ("2. Agregar un país")
    print ("3. Modificar un país")
    print ("4. Buscar un país")
    print ("5. Filtrar países")
    print ("6. Ordenar países")
    print ("7. Estadísticas")
    print ("8. Salir")



    