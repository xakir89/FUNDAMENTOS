print("""
********************************************
*                                          *
*   Una institución educativa le paga a    *
*   sus profesores $ 30000  la hora y le   *
*   hace un descuento del 5% por concepto  *
*   de ahorro.                             *
*                                          *
*   Elaborar un algoritmo para determinar  *
*   el monto del descuento y el monto      *
*   total a pagar.                         *
*                                          *
********************************************
""")

def horast():
    x = float(input("Horas Trabajadas por Docente: "))
    return x

def salario():
    bandera = True
    while bandera:
        horas = horast()
        if horas < 0:
            print("Las Horas no pueden ser negativas")
        else:    
            sal =  horas * 50000
            des = sal * 0.05
            totalp = sal - des
            bandera = False
    return totalp, sal, des,horas

def tablero():
    to,sal,des,horas = salario()
    print(f"""
********************************************
*                                          *
*       SALARIO DOCENTE HORA CATEDRA       *
*                                          *
*          HORAS TRABAJADAS: $ {horas}       *
*          SALARIO DOCENTE: $ {sal}    *
*          DESCUENTO AHORRO: $ {des}    *
*                                          *
*          TOTAL A PAGAR: $ {to}      *
*                                          *
********************************************
""")
def main():
    bandera = True
    while bandera:
        print(f"""
********************************************
*                                          *
*               OPCIONES                   *
*                                          *
*          1. INGRESO HORAS                *
*          2. SALIR                        *
*                                          *
********************************************
""")
        opc = int(input("Ingrese Una Opcion: "))
        if opc == 1:
            tablero()
        else:
            if opc ==2:
                print("Gracias por Confiar en nosotros")
                bandera = False
            else:
                print("DATO ERRADO")
                
main()
