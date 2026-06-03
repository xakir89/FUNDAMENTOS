###################################################################################################
#   8. Elaborar un algoritmo que teniendo el tipo de empleado y su sueldo, calcule el incremento  #
#   salarial y el valor del nuevo sueldo; si se conoce que a los empleados tipo 1 y 2, se les     #
#   aumenta un 5%; y a los tipo 3 y 4 el 12%. El algoritmo debe imprimir el sueldo más aumento.   #
###################################################################################################

empleado = int(input("Tipo empleado 1 2 3 o 4: "))

while empleado<1:
    empleado = int(input("Tipo empleado 1 2 3 o 4: "))
while empleado>4:
    empleado = int(input("Tipo empleado 1 2 3 o 4: "))

sueldo = int(input("Sueldo del empleado: "))

while sueldo<9999:
    print("El sueldo no puede ser menor a 9999")
    sueldo = int(input("Sueldo del empleado: "))
    

if empleado < 3:
    aumento = sueldo * 0.05
    total = sueldo + aumento
    print(f"el sueldo del empleado es {sueldo} mas el aumento del 5% {aumento}\ntotal a ganar: {total}")
else:
    aumento = sueldo * 0.12
    total = sueldo + aumento
    print(f"el sueldo del empleado es {sueldo} mas el aumento del 12% {aumento}\ntotal a ganar: {total}")



    




