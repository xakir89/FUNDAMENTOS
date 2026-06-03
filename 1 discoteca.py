#####################################################################################################################################
# Ejercicio 1: El Guardia de Seguridad (El que mencionamos antes) Estás programando la entrada a un club nocturno.                  #
# El programa recibe dos datos de la persona: Su edad (un número).Si tiene_pase_vip (puede ser Verdadero o Falso).                  #
# Las reglas del club son:                                                                                                          #
# Una persona puede entrar si tiene 18 años o más. Sin embargo, si la persona tiene un pase VIP, puede entrar sin importar su edad. #
# Tu tarea: Escribe la estructura condicional (if / else) con los operadores lógicos correctos (AND, OR)                            #
# que determine si la persona "Entra" o "No entra".                                                                                 #
# ###################################################################################################################################
def edad():
    edad = int(input("Ingrese Edad: "))
    while edad < 15:
        print("la edad debe ser minimo desde 15 años")
        edad = int(input("Ingrese Edad: "))
    return edad

def vip():
    vip = int(input("ingrese 1 es vip  o 2 no es vip: "))
    while vip <1:
        vip = int(input("ingrese 1 es vip  o 2 no es vip: "))
    while vip>2:
        vip = int(input("ingrese 1 es vip  o 2 no es vip: "))
    return vip

def inicio():
    ed=edad()
    vi=vip()
    if vi ==1:
        print ("el usuario es VIP")
        print(f"No importa si el usuario es menor de edad el usuario puede ingresar.")
    if vi ==2:
        print ("el usuario no es VIP")
        if ed >= 18:
            print ("el usuario es mayor de edad y puede ingresar")
        else:
            print ("el usuario es menor de edad No puede Ingresar")
inicio()





