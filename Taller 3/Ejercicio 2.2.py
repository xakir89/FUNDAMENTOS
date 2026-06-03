#Diseñe un algoritmo que imprima en pantalla el conjunto de los divisores de un
#número entero (x) digitado por el usuario.
x = int(input("Digita Numero para hallar sus divisores:"))
valido = x != 0

if valido:
    con_div = 0
    print(f"\nLos divisores de {x} son:\n")
    for i in range(1, abs(x) + 1):
        if x % i == 0:
            print(f"{i} Es Divisor de {x}")
            con_div = con_div + 1
    print(f"\nTotal de divisores encontrados: {con_div}")
else:
    print("Error: El número cero tiene infinitos divisores.")
