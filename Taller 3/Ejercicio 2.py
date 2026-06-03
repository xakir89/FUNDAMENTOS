#Diseñe un algoritmo que imprima en pantalla el conjunto de los divisores de un
#número entero (x) digitado por el usuario.

# Entrada de datos
x = int(input("Digita el número para hallar sus divisores: "))

# Bandera para validar que el número no sea cero (no se puede dividir por 0)
es_valido = x != 0

if es_valido:
    contador_divisores = 0
    print(f"\nLos divisores de {x} son:")
    
    # El rango va desde 1 hasta el valor absoluto de x
    # Usamos abs(x) por si el usuario digita un número negativo
    for d in range(1, abs(x) + 1):
        
        # Proposición lógica: ¿El residuo de x entre d es cero?
        if x % d == 0:
            print(f"-> {d}")
            
            # Contador: suma 1 cada vez que encuentra un divisor
            contador_divisores = contador_divisores + 1
            
    print(f"\nTotal de divisores encontrados: {contador_divisores}")
else:
    print("Error: El número cero tiene infinitos divisores.")
