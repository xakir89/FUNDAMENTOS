# Elaborar un algoritmo que convierta una medida de longitud en kilometros 
# a metros, centímetros, milímetros, pulgadas, yardas, millas y pies
import time
def ingreso():
    while True:
        try:
            k = float(input("Ingresa cantidad de Kilometros: "))
            if k > 0:
                return k
                break
            else:
                print("Dato Errado debe ser mayor a  0 ")
                print("...")
                k = int(input("Ingresa cantidad de Kilometros: "))
        except ValueError:
            print(f"Error entrada no valida solo puede ingresar números")
            print("...")

def operaciones():
    kilometros = ingreso()
    metros = kilometros * 1000 
    centimetros = kilometros * 100000
    milimetros = kilometros * 1000000
    pulgadas = kilometros * (100000/2.54) # 1 PULGADA EQUIVALE A 2,54 CENTIMETROS
    pies = kilometros * ((100000/2.54)/12) # 1 PIE EQUIVALE A 12 PULGADAS
    yardas = kilometros * (((100000/2.54)/12)/3) # 1 YARDA EQUIVALE A 3 PIES
    millas = kilometros * ((((100000/2.54)/12)/3)/1760) # 1 MILLA EQUIVALE A 1760 YARDAS
    return kilometros, metros, centimetros, milimetros,pulgadas, pies, yardas, millas

def tablero(k,m,c,mm,p,pi,y,mi):
    print(f"""
************************************
*   Kilometros Recorridos:  {k:.2f}  *
*          CONVERSION A:           *
*     Metros:       {m:.2f}       *
*     Centimetros:  {c:.2f}     *
*     Milimetros:   {mm:.2f}    *
*     Pulgadas:     {p:.2f}      *
*     Pies:         {pi:.2f}       *
*     Yardas:       {y:.2f}       *
*     Millas:       {mi:.2f}          *
*                                  *
************************************
""")
    time.sleep(4)
    
def main():
    while True:
        print("*"*30)
        print(f"{'OPCIONES':^30}")
        print("*"*30,"\n")
        print(f"{'1. Calcular':^30}")
        print(f"{'2. Salir   ':^30}\n")
        print("*"*30)
        try:
            opc = int(input("Ingrese una opcion: "))
            if opc == 1:
                k,m,c,mm,p,pi,y,mi = operaciones()
                tablero(k,m,c,mm,p,pi,y,mi)
            elif opc == 2:
                print("Gracias por usar nuestro servivio")
            else:
                print("Dato Errado solo puede ingresar 1 o 2")
                print("...")
        except ValueError:    
            print("No ingrese Simbolos ni letras solo puede ingresar 1 o 2")
            print("...")

main()
