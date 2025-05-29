# QuickSort
# 
# Reto    0  1 2
import random


lista = [random.randint(-1000, 1000) for x in range(10) ]
print(lista)
print()
#Proceso
def ordenar():
    for izq in range(len(lista)-1):
        for der in range(izq + 1, len( lista)):
            if lista[izq] > lista[der]:
                tem = lista[izq]
                lista[izq] = lista[der]
                lista[der] = tem
            pass
        print(f"der: {lista}")
    print(f"izq: {lista}")

ordenar()