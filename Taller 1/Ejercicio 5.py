# Elaborar un algoritmo que tome como argumento tres números y retorne la suma
# de los cuadrados de estos números. 

def ingreso():
    x = int(input(f"Ingrese un numero de 3 digitos: "))
    print()
    bandera = True
    while bandera:
        if 99 < x < 1000:
            return x
            bandera = False
        else:
            print("Número no válido, Debe ser un número de 3 dígitos.")
            x = int(input(f"Ingrese un numero de 3 digitos: "))
            print()

def separar(x):
    u = x % 10
    d = (x%100)//10
    c = x//100
    return u,d,c

def operacion(u, d, c):
    suma_cuadrados = u**2 + d**2 + c**2
    return suma_cuadrados

def Tablero(u,d,c,sc,x):
    print(f"""
    ******* DATOS INGRESADOS PARA LA SUMA DE CUADRADOS *******
    *                    INGRESO = {x}                       *
    *                                                        *
    *     UNIDAD  = {u} DECENA = {d} CENTENA = {c}                 *
    *                                                        *
    *              2   2   2                                 *
    *             {u} + {d} + {c}  = {sc}                           *
    *                                                        *
    **********************************************************
    """)

def main():
    while True:
        print("""
        ************************** MENU **************************
        *                                                        *
        *                1. Ingresar un Numero de                *
        *                    3 cifras                            *
        *                2. Salir                                *
        *                                                        *
        **********************************************************
        """)
        opc = int(input("Ingrese Una opcion 1 o 2: "))
        print()
        if opc == 1:
            x = ingreso()
            u,d,c= separar(x)
            sc = operacion(u,d,c)
            Tablero(u,d,c,sc,x)

        elif opc == 2:
            print("Gracias por Confiar en Nosotros")
            print()
            break
        else:
            print("Dato errado solo se puede ingresar 1 o 2")

main()
