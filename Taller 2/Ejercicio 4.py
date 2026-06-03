####################################################################################################
#                                                                                                  #
#   4. Elaborar un algoritmo que lea dos números ingresados por el usuario, si la suma de los dos  #
#   números es negativa, mostrar su promedio , de lo contrario mostrar si el resultado es par o    #
#   impar.                                                                                         #
#                                                                                                  #
####################################################################################################


# 1. Entrada de datos
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# 2. Cálculo de la suma
suma = num1 + num2

# 3. Lógica de decisión
if suma < 0:
    # Si es negativa, calculamos el promedio
    promedio = suma / 2
    print(f"La suma es negativa ({suma}). El promedio es: {promedio}")
else:
    # Si es positiva o cero, verificamos si es par o impar
    # Usamos lógica matemática: ¿Es el residuo de suma/2 igual a 0?
    if suma % 2 == 0:
        print(f"La suma es {suma} y es un número PAR.")
    else:
        print(f"La suma es {suma} y es un número IMPAR.")
