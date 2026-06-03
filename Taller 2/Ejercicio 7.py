###################################################################################################
#  7. Elaborar un algoritmo que solicite un número de día de entre 1 y 7; e imprima el día de la  #
#       semana correspondiente.                                                                   #
###################################################################################################

x = int(input("Ingrese un número del 1 al 7: "))

while x < 1:
    print("Número inválido")
    x = int(input("Ingrese nuevamente un número del 1 al 7: "))
while x > 7:
    print("Número inválido")
    x = int(input("Ingrese nuevamente un número del 1 al 7: "))
if x == 1:
    print("Lunes")
if x == 2:
    print("Martes")
if x == 3:
    print("Miércoles")
if x == 4:
    print("Jueves")
if x == 5:
    print("Viernes")
if x == 6:
    print("Sábado")
if x == 7:
    print("Domingo")
    




