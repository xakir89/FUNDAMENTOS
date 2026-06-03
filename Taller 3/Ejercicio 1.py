#Diseñe un algoritmo que imprima en pantalla el conjunto de los (n)
#múltiplos de número entero (x) digitado por el usuario.

# Entrada de datos
x = int(input("Digita el número base (x): "))
n = int(input("¿Cuántos múltiplos quieres ver? (n): "))

# Uso de una Bandera (Boolean)
es_valido = n > 0

if es_valido:
    acumulador_suma = 0
    print(f"\nLos primeros {n} múltiplos de {x} son:")
    
    # El ciclo 'for' genera el conjunto k = {1, 2, ..., n}
    for k in range(1, n + 1):
        multiplo = x * k
        print(f"Múltiplo {k}: {multiplo}")
        
        # Acumulador: suma el múltiplo actual al total
        acumulador_suma = acumulador_suma + multiplo
    
    print(f"\nLa suma total del conjunto es: {acumulador_suma}")
else:
    print("Error: La cantidad de múltiplos (n) debe ser mayor a 0.")
