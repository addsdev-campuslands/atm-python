palabras = []

palabras.append("Python")
palabras.append(5)
palabras.append(True)
palabras.append(input("Ingrese un descripcion!:"))

palabras.insert(0, "ID: 2")

print("Por elementos:")
for item in palabras:
    print(item)

palabras[3] = False

print("Por elementos despues del Update:")
for item in palabras:
    respuesta = input(f"Quiere actualizar el valor de: {item}\ns\\n")
    if respuesta == "s":
        # palabras[x] = ""
        item = input("Ingrese el nuevo valor:")
    # Ver en consola los cambios, si hay!
    print(f"Valor nuevo: {item}")

print("Por elementos final:")
for item in palabras:
    print(item)

# for indice in range(len(palabras)): # 0,1,2,3... [0,1,2,3,4.....]
#     print(indice)
#     print(type(indice))
#     print(palabras[indice])
#     print(type(palabras[indice]))