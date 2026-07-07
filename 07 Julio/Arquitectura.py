def ingreso(v):
    x = float(input(f"Ingrese Valor para {v: }"))
    return x
def operacion():
    BM = ingreso("Base Mayor")
    bm = ingreso("Base Menor")
    am = ingreso("Altura Menor")

    AM = (BM/bm)*am

    return BM, bm, am, AM

def menu():
    print("""
*************************************
*                                   *
*      CALCULADORA DE ALTURA        *
*                                   *
*       1. INGRESAR VALORES         *
*       2. SALIR                    *
*                                   *
*************************************
""")
    opc = int(input("Ingrese opcion 1 o 2: "))
    while True:
        if opc == 1:
            BM, bm, am, AM = operacion()
            if opc == 2:
                print("Gracias por la Confianza")
                break
        else:
            print("Dato Errado")
            
            
def tablero():
    
    menu()
    print("""
*************************************
*                                   *
*      CALCULADORA DE ALTURA        *
*                                   *
*          AlTURA EDIFICIO          *
*       BM        *
*                                   *
*************************************

""")
