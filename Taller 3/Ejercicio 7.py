#7. Diseñe un algoritmo que permita calcular si un número es primo o no, recuerde
#que los ńmeros primos son aquellos que solo son divisibles por la unidad y por
#ellos mismos.


def primo(x):                
    contador = 0
    for i in range(1, x + 1):
        if  x % i == 0:
            contador =contador + 1

    if contador == 2:
        print("El número es primo")
    else:
        print("El número no es primo")
n = int(input("Ingrese un número: "))
primo(n)
