def Dato(VARIABLE_NUMERO):
    print("INGRESA EL DATO PARA REALIZAR EL EJERCICIO:")
    x = float(input(f"Digita Su numero para {VARIABLE_NUMERO}"))
    return x
def perimetro(a,b,c):
    p = (a+b+c)/2
    return p
def area(p,a,b,c):
    A = (p * (p-a) * (p-b) * (p-c) ) ** 0.5
    return(A)

def tablero(A,p,a,b,c):
    print(f"""
    ********************AREA Y SEMIPERIMETRO********************
    *                                                          *
    *                     _________________                    *
    *             ÁREA = √ p(p-a)(p-b)(p-c) = {A:.2f}             *
    *                                                          *
    *             SEMIPERIMETRO = (a+b+c)                      *
    *                            --------- = {p:.2f}              *
    *                                2                         *
    *                                                          *
    ************************************************************
    """)
def main():
    print("**********AREA Y SEMIPERIMETRO DATOS DE INGRESO**********")

    a = Dato("a: ")
    while a < 0:
        print("Error los datos que debes ingresar deben ser positivos o cero")
        a = Dato("a: ")
    b = Dato("b: ")
    while b < 0:
        print("Error los datos que debes ingresar deben ser positivos o cero")
        b = Dato("b: ")
    c = Dato("c: ")
    while c < 0:
        print("Error los datos que debes ingresar deben ser positivos o cero")
        c = Dato("a: ")

    p = perimetro(a,b,c)
    A = area(p,a,b,c)

    tablero(A,p,a,b,c)
main()
    
