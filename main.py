# Ingresar una cifra X y vamos a calcular cuantos 
# billetes de 50k, 20k, 10k y 5k tenemos que devolverle al usaurio

dinero_disponible = [10, 8, 10, 0]

def mostrarDisponible(montos):
    print(f"Disponible  💸")
    print(f"50k: {montos[0]}\n20k: {montos[1]}",
      f"\n10k: {montos[2]}\n5k: {montos[3]}")
    
def validarMonto(denominacion):
    cantidad = -1
    while True:
        cantidad = int(input("Ingrese la cantidad de $ a retirar: "))
        if not cantidad % denominacion == 0:
            input("Ingrese un monto valido\nEste ATM solo " +
              f"admite valores multiplos de {denominacion} COP\nEnter para continuar....")
        else:
            return cantidad
        
def validarDenominacionMenor(denominacion):
    can = len(denominacion)
    minima = 0
    for item in range(can): # [0,1,2,3,4..]
        
        if denominacion[item] > 0:
            if item == 0:
                minima = 50_000
            elif item == 1:
                minima = 20_00
            elif item == 2:
                minima = 10_000
            else:
                minima = 5_000
    return minima
    
denominacion = validarDenominacionMenor(denominacion= dinero_disponible)
print(f"La minima: {denominacion}")

mostrarDisponible(montos= dinero_disponible)

cantidad = validarMonto(denominacion=denominacion)
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

