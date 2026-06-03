#######################################################################################################
#   9. Diseñe un algoritmo que convierta un número entero positivo, menor a 257 a sistema binario.    #
#######################################################################################################


x = int(input("Ingrese un Número de 0 a 256: "))

# Validaciones
while x < 0:
    print("\nEl valor ingresado no debe ser negativo")
    x = int(input("Ingrese un Número de 0 a 256: "))

while x > 256:
    print("\nEl valor ingresado no debe ser mayor de 256")
    x = int(input("Ingrese un Número de 0 a 256: "))

if x ==0:
    print("Binario es : 0")
else:
    numero=x
    binario = ""
    for i in range(9):
        residuo = x%2
        binario = str(residuo) + binario
        x = x//2
    print(f"en Binario {numero} es {int(binario)} ")
