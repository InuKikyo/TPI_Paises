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

#Opcion 2. Agregar un país
def agregar(paises):

    nombre = input("Ingrese el nombre del país que desea agregar: ")
    try:
        poblacion = int(input("Población: "))
        superficie = int(input("Superficie: "))
    except ValueError:
        print ("Solo ingrese números.")
    
    continente = input("Continente: ")
    paises.append({"nombre": nombre,
                    "poblacion": poblacion,
                    "superficie": superficie,
                    "continente": continente})
    
    print ("País agregado exitosamente.")


#Opcion 3. Modificar un pais
def modificar(paises):
    nombre = input("País que desea modificar: ").lower()

    for pais in paises:
        if pais["nombre"].lower() == nombre:
            print ("1. Población: ")
            print ("2. Superficie: ")

            opcion = input("Seleccione una opción: ")
            
            try:
                if opcion == "1":
                    pais["poblacion"] = int(input("Población del nuevo país: "))
                elif opcion == "2":
                    pais["superficie"] = int(input("Superficie del nuevo país: "))
                else:
                    print ("Opción inválida.")
                    return
                
                print ("País actualizado exitosamente.")
            except ValueError:
                print ("Ingrese solo números.")
                return
    print ("País no encontrado")


#Opcion 4. Buscar un pais
def buscar(paises):

    nombre = input("Ingrese el nombre del país que desea buscar: ").lower()
    encontrados = []

    for pais in paises:
        if nombre in pais["nombre"].lower():
            encontrados.append(pais)
    
    if encontrados:
        for pais in encontrados:
            print (pais)
    else:
        print ("No se pudo encontrar el país.")


#Opcion 5. Filtrar paises por continente
def filtrar(paises):

    continente = input("Ingrese un continente: ").lower()
    encontrados = []

    for pais in paises:
        if pais["continente"].lower() == continente:
            encontrados.append(pais)

    mostrar(encontrados)


#Opcion 6. Ordenar paises
def ordenar(paises):

    print ("1. Nombre: ")
    print ("2. Población: ")
    print ("3. Superficie: ")

    opcion = input("Ordenar países por: ")

    if opcion == "1":

        for i in range(len(paises)):
            for j in range(i + 1, len(paises)):
                if paises[i]["nombre"] > paises[j]["nombre"]:
                    aux = paises[i]
                    paises[i] = paises[j]
                    paises[j] = aux
    elif opcion == "2":

        for i in range(len(paises)):
            for j in range(i + 1, len(paises)):
                if paises[i]["poblacion"] > paises[j]["poblacion"]:
                    aux = paises[i]
                    paises[i] = paises[j]
                    paises[j] = aux
    elif opcion == "3":

        for i in range(len(paises)):
            for j in range(i + 1, len(paises)):
                if paises[i]["superficie"] > paises[j]["superficie"]:
                    aux = paises[i]
                    paises[i] = paises[j]
                    paises[j] = aux
    else:
        print ("Opción inválida.")
        return

    mostrar(paises)





#Menú
def mainmenu():
    print ("\n=====Menú=====")
    print ("1. Mostrar países")
    print ("2. Agregar un país")
    print ("3. Modificar un país")
    print ("4. Buscar un país")
    print ("5. Filtrar países por continente")
    print ("6. Ordenar países")
    print ("7. Estadísticas")
    print ("8. Salir")



    