##########################################################################
# Diseñe aun algoritmo que imprima las siguientres series para n terminos#
#               a, + 1/2, - 3/4, + 5/6, -7/8, +9/10...                   #
##########################################################################

n = int(input("Ingrese el número de términos: "))

for i in range(1, n + 1):
    # Lógica para los números
    numerador = 2 * i - 1
    denominador = 2 * i
    
    # Lógica para determinar la variable 'signo'
    if i % 2 == 0:
        signo = "-"
    else:
        signo = "+"
    
    # Imprimimos usando la variable signo
    print(f"{signo} {numerador}/{denominador}", end=" ")

print("...") # Salto de línea final
print("")

##########################################################################
#               b, + 1/2! - 3/4! + 5/6! -7/8! +9/10!...                  #
##########################################################################

for i in range(1, n + 1):
    # 1. Definimos los números base para la fracción
    numerador = 2 * i - 1
    denominador = 2 * i
    
    # 2. Lógica para calcular el FACTORIAL (mera lógica matemática)
    # Reiniciamos el factorial en 1 para cada término de la serie
    factorial = 1
    for j in range(1, denominador + 1):
        factorial = factorial * j
    
    # 3. Lógica para la variable SIGNO
    if i % 2 == 0:
        signo = "-"
    else:
        signo = "+"
    
    # 4. Impresión de la fracción con el formato de la imagen (con !)
    # Usamos base_denominador para mostrar "2!", "4!", etc.
    print(f"{signo} {numerador}/{factorial}", end=" ")

print("...") # Salto de línea final
print("")

##########################################################################
#               c, + 1/2 - 3^4/4 + 5^6/6 -7^8/8 +9^10/10...              #
##########################################################################


for i in range(1, n + 1):
    # 1. Definimos la base del numerador y el denominador
    base_numerador = 2 * i - 1
    denominador = 2 * i
    
    # 2. Lógica para calcular la POTENCIA (base^exponente)
    # Según la imagen, el exponente es igual al denominador
    exponente = denominador
    potencia_resultado = 1
    
    for j in range(1, exponente + 1):
        potencia_resultado = potencia_resultado * base_numerador
    
    # 3. Lógica para la variable SIGNO
    if i % 2 == 0:
        signo = "-"
    else:
        signo = "+"
    
    # 4. Impresión de la fracción con el formato de potencia
    # Usamos el símbolo ^ para representar la potencia visualmente
    if i == 1:
        # El primero suele mostrarse simple, pero sigamos el patrón de la imagen
        print(f"{signo} {base_numerador}/{denominador}", end=" ")
    else:
        print(f"{signo} {potencia_resultado}/{denominador}", end=" ")

print("...") # Salto de línea final
print()

##########################################################################
#               d, - 1/5 - 3/10 + 5/15 + 7/20 -9/25 - 11/30...           #
##########################################################################

# Variable auxiliar para controlar el ciclo de 4 signos
# 1 y 2 seran menos, 3 y 4 seran mas
control_signo = 1

for i in range(1, n + 1):
    # 1. Lógica de números
    numerador = 2 * i - 1
    denominador = 5 * i
    
    # 2. Lógica de variable 'signo' (Patrón: - - + +)
    if control_signo == 1:
        signo = "-"
    if control_signo == 2:
        signo = "-"
    if control_signo == 3:
        signo = "+"
    if control_signo == 4:
        signo = "+"
    
    # 3. Imprimimos la fracción
    print(f"{signo} {numerador}/{denominador}", end=" ")
    
    # 4. Actualizamos el control de signo para la siguiente vuelta
    if control_signo == 4:
        control_signo = 1  # Reiniciamos el ciclo
    else:
        control_signo = control_signo + 1

print()


