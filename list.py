# Lista de InuUtiles Escolares
# Agregar nuevos utiles
# Listar todos los utiles
# Actualizar un item por la posicion
# Eliminar un item por la posicion

utiles = []
item = []
menu = """
·················································
:                                               :
:                                               :
:   /$$      /$$                                :
:  | $$$    /$$$                                :
:  | $$$$  /$$$$  /$$$$$$  /$$$$$$$  /$$   /$$  :
:  | $$ $$/$$ $$ /$$__  $$| $$__  $$| $$  | $$  :
:  | $$  $$$| $$| $$$$$$$$| $$  \\ $$| $$  | $$  :
:  | $$\\  $ | $$| $$_____/| $$  | $$| $$  | $$  :
:  | $$ \\/  | $$|  $$$$$$$| $$  | $$|  $$$$$$/  :
:  |__/     |__/ \\_______/|__/  |__/ \\______/   :
:                                               :
: 1. Agregar nuevos Utiles Inutiles             :
: 2. Listar los Utiles Inutiles                 :
: 3. Actualizar un Util Inutil                  :
: 4. Eliminar un Util Inutil                    :
: 5. Finalizar                                  :
·················································
"""

def mostrarUtiles(listaDeUtiles):
    print("+-------------------------------------+")
    print(" 📚  Lista de Utiles Inutiles   ")
    print("+-------------------------------------+")
    for index, util in enumerate(listaDeUtiles):
        print(f"{index + 1} - Nombre: {util[0]}  Cantidad: {util[1]}")
        print("-------------------------------------")

def agregarUtiles():
    nombre = input("Ingrese el nombre del Util Inutil: \n")
    cantidad = int(input(f"Ingrese la cantidad de {nombre} :\n"))
    item.append(nombre)
    item.append(cantidad)
    utiles.append(item.copy())
    print(utiles)
    item.clear()

def modificarUtiles():
    itemNombre = input("Ingrese el nombre del Util Inutil a Buscar:\n")
    for utilIndex in range(len(utiles)):
        if utiles[utilIndex][0] == itemNombre:
            nuevoNombre = input(f"Ingrese el nuevo valor para {utiles[utilIndex][0]}: \n")
            utiles[utilIndex][0] = nuevoNombre

def eliminarUtiles():
    itemPosicion = int(input("Ingrese la posicion del Util Inutil: \n")) - 1
    itemEliminado = utiles.pop(itemPosicion)
    print(f"El Util Inutil elimado fue: {itemEliminado[0]}")

while True:
    print(menu)
    opcion = int(input("Selecciona una opcion del menu: \n"))
    if opcion == 1:
        agregarUtiles()
    elif opcion == 2 :
        mostrarUtiles(utiles)
    elif opcion == 3:
        mostrarUtiles(utiles)
        modificarUtiles()
    elif opcion ==4:
        mostrarUtiles(utiles)
        eliminarUtiles()
        pass
    elif opcion == 5: 
        break
        