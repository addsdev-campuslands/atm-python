# Ingresar una cifra X y vamos a calcular cuantos 
# billetes de 50k, 20k, 10k y 5k tenemos que devolverle al usaurio

denominacion = ([5_000, "Cinco Mil"], [10_000, "Diez Mil"], [20_000, "Veinte Mil"], [50_000, "Cincuenta Mil"])
#             [cantidad,posicion en denominacion]
dinero_disponible = [[10, 0], [8, 1], [0, 2], [5, 3]]

def mostrarDisponible(montos: list):
    print(f"Disponible  💸")
    for d in montos:

        print(f"{denominacion[d[1]][1]} -> {d[0]} \n")
    
def validarMonto(denominacion):
    cantidad = -1
    while True:
        cantidad = int(input("Ingrese la cantidad de $ a retirar: "))
        if not cantidad % denominacion == 0:
            input("Ingrese un monto valido\nEste ATM solo " +
              f"admite valores multiplos de {denominacion} COP\nEnter para continuar....")
        else:
            return cantidad
        
def validarDenominacionMenor(listaDenominacion): #[cantidad, posicion]
    minima = 0
    for d in listaDenominacion[::-1]:
        if d[0] > 0:
            #  denominacion[d[1]] = [5_000, "Cinco Mil"]
            # denominacion[d[1]][1] = "Cinco Mil"
            # denominacion[d[1]][1] = 5_000
            minima = denominacion[d[1]][0]
            print(f'validarDenominacionMenor: {minima}')
    return minima

def validarTotalDisponible():
    #Antes de "Retirar" podamos validar que el cajero cuente con ese monto disponible
    pass
    
denominacionMinima = validarDenominacionMenor(listaDenominacion= dinero_disponible)
print(f"La minima: {denominacionMinima}")

mostrarDisponible(montos= dinero_disponible)

cantidad = validarMonto(denominacion=denominacionMinima)
#230.000

can_50 = 0
can_20 = 0
can_10 = 0
can_5 = 0
total = cantidad

# Que la cantidad ya es valida!! 

while total > 0:

    if total >= 50_000:
        # can_50 += 1
        can_50 = can_50 + 1
        # total -= 50000
        total = total - 50_000
        dinero_disponible[0] -= 1
        #dinero_disponible[0] = dinero_disponible[0] - 1
    elif total >= 20_000:
        can_20 += 1
        total -= 20_000
        dinero_disponible[1] -= 1
    elif total >= 10_000:
        can_10 += 1
        total -= 10_000
        dinero_disponible[2] -= 1
    elif total >= 5_000:
        can_5 += 1
        total -= 5_000
        dinero_disponible[3] -= 1
    else:
        print("No tenemos fondos suficientes :c")
        break

print(f"Cantidad de dinero: {cantidad}\n50k: {can_50}\n20k: {can_20}",
      f"\n10k: {can_10}\n5k: {can_5}")

mostrarDisponible(montos= dinero_disponible)

