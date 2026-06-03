############################################################################################
#                                                                                          #
#   5. Elaborar un algoritmo que lea cuatro números ingresados por el usuario y los sume,  #
#   descartando los negativos.                                                             #
#                                                                                          #
############################################################################################


# 1. Entrada de datos
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))
d = int(input("Ingresa el Cuarto número: "))

suma=0

if a>0:
    suma+=a    
if b>0:
    suma+=b
if c>0:
    suma+=c  
if d>0:
    suma+=d
if suma>0:
    print("la suma de los numeros positivos es =",suma)
else:
    print("los numeros son negativos por ende no se suman")

    
