#          0 a 25         26 a 50             51   a 80           > 81
score = (["BAJO", 0, 25], ["ACEPTABLE", 26, 50], ["SOBRESALIENTE", 51, 80], ["EXCELENTE", 81, 100])

# print(score[:]) # Todos
# print(score[1:]) # Todas menos la 0 :c
# print(score[:-1]) # Todas menos la Ultima :c
# print(score[1:-1]) # 1,2,3
# print(score[1:-1:2])# 1,3
# print(score[::-1])# Orden inverso

inversa = score[::-1]

# print()
# print(inversa)
# print(score)


#(0, score[0]), (1, score[1])

def funcion(nota):
    for i, n in enumerate(score, start= 1):
        if(nota >= n[1] and nota <= n[2]):
            print(f"La nota es: {i} - {n[0]}")
            break

def promedios():
    mensaje = "📚 Notas: \n"
    for i, n in enumerate(score, start= 1):
        #nombre = n[0]
        #min = n[1]
        #max = n[2]

        nombre, min, max = n
        #                                                              n[1:]
        mensaje += promedioNota(posicion= i, nombre= nombre, rango= [min, max]) + "\n"
        #mensaje += f"{i}. {n[1]} a {n[2]} -> {n[0]} \n"
    return mensaje

def promedioNota(posicion: int, nombre: str, rango: list):
    return f"{posicion}. {rango[0]} a {rango[1]} -> {nombre}"

nota = float(input("Ingrese la nota: "))
print(promedios())
funcion(nota)

# Pedir una nota al usuario entre 1 al 100
# Calcular cual seria su Rango de Nota
#print(score) # (....)
#print(score[0]) # [...]
#print(score[0][0])# Texto
#print(score[0][1])# Numero


