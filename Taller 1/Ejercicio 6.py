# Elaborar un algoritmo para calcular el IVA (16%) de un valor ingresado por teclado. 
# Ejemplo: valor digitado => 2000
# Mostrar en pantalla IVA = 320 y valor mas IVA = 2320.

def  ingreso():
    while True:
        try:
            x=int(input(f"Ingrese el valor para calcular iva: "))
            print("...")
            if x >= 2000:
                break
            else:
                print(f"Ingrese un valor mayor a 2000 para calcular iva: ")
                print("...")
        except ValueError:
            print(f"Error entrada no valida solo puede ingresar números")
            print("...")
    print(f"Numero valido ingresado: {x}\n...")
    return x

def calcular():
    x = ingreso()
    iva = x * 0.16
    total = iva + x
    return x,iva, total

def tablero(x, iva, total):
    print("-"*49)
    print(f"|{'INGRESO':^15}|{'IVA':^15}|{'TOTAL':^15}|")
    print("-"*49)
    print(f"|{x:^15,.1f}|{iva:^15,.1f}|{total:^15,.1f}|")

def mostrar_histaorial(historial):
    if not historial:
        print("Nose realizaron operaciones en esta Sesion.")
        print("...")
        return
    print("\n=== RESUMEN DE OPERACIONES REALIZADAS ===")
    print("-"*49)
    print(f"|{'INGRESO':^15}|{'IVA':^15}|{'TOTAL':^15}|")
    print("-"*49)
    for h_x, h_iva, h_t in historial:
        print(f"|{h_x:^15,.1f}|{h_iva:^15,.1f}|{h_t:^15,.1f}|")
    print("-"*49)
    print("...")

def main():
    historial = []

    while True:
        print("-"*49)
        print(f"|{'MENU':^47}|")
        print(f"|{'1. CALCULAR IVA':^47}|")
        print(f"|{'2. SALIR':^47}|")
        print("-"*49)
        print()
        try:
            opc = int(input("Ingrese una opcion 1 o 2: "))
            if opc == 1:
                x, iva, total = calcular()
                tablero(x,iva,total)
                historial.append((x,iva,total))
                print("...")
            elif opc == 2:
                print("Gracias por usar nuestros servicios")
                print("...")
                mostrar_histaorial(historial)
                break
            else:
                print("...")
                print("Dato errado solo puede ser 1 o 2")
                print("...")
                
        except ValueError:
            print(f"Error entrada no valida solo puede ingresar números")
            print("...")
main()

        