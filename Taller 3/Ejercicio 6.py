#6. Diseñe un algoritmo que capture 10 números y al final imprima el promedio de estos.

def promedio():
    n=int(input("Ingrese cantidad de notas para calcular el promedio:"))
    x = 0
    for i in range(1, 1+n):
        numero = float(input(f"ingrese Nota {i} Numero:"))
        x = numero+x
    return x/n
pro=promedio()
print("promedio de Notas:",pro)
