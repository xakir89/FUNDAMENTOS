def solicitud_numero(variable_numero):
    """Solicita un Numero al usuario de Forma Segura"""
    x = float(input(f"Digita Su numero para {variable_numero}"))
    print()
    return x        
        
def ej5(a,b):
    if a >= 0 and b >= 0:
        x = a**0.5 + b**0.5
        return x
    return None

def ej1(A):
    if A != 5:
        x = (100-200)/(A-5)        
        return x
    return None
    
def ej2(A):
    x =  15 - (A**2/3)
    return x

def ej3(a,b,c):
    x = a**2 + b**2 -35 * c
    return x

def ej4(X):
    E = 5*X**2-3*X+5
    return E

def ej6(a):
    x = a**10-5    
    return x

def tablero(A,a,b,c,X,r1,r2,r3,r4,r5,r6):
    if r1 != None:
        res1 = f"{r1:.1f}"
    else:
        res1 = "(A = 5 No Valido)"

    if r5 != None:
        res5 = f"{r5:.1f}"
    else:
        res5 = "No Real"

    print(f"""
    *****************************************************************
    *              EJERCICIOS PUNTO NUMERO1 TALLER                  *
    *                                             2                 *    
    *  a. 100 - 200                    b.     15 - A                *
    *     ---------  = {res1}                ---  = {r2:.1f}  *
    *       A - 5                              3                    *
    *                                                               *
    *        2   2                             2                    *
    *  c.   a + b - 35c  = {r3:.1f}  d.    5 X - 3 X + 5  = {r4:.1f}     *
    *                                                               *
    *        __   __3                                                *
    *  e.   √a + √b  = {res5}                                          *
    *                                                               *
    *         10                                                    *
    *  f.    a - 5  = {r6:.1f}                                     *
    *                                                               *
    * A en el primer ejercicio no puede ser 5 ya que daria una      *
    *  divicion por 0 el denominador debe ser diferente de 0        *
    *****************************************************************
           """)
def main():
    A = solicitud_numero("A: ")
    a = solicitud_numero("a: ")
    b = solicitud_numero("b: ")
    c = solicitud_numero("c: ")
    X = solicitud_numero("X: ")

    r1 = ej1(A)
    r2 = ej2(A)
    r3 = ej3(a,b,c)
    r4 = ej4(X)
    r5 = ej5(a,b)
    r6 = ej6(a)

    tablero(A,a,b,c,X,r1,r2,r3,r4,r5,r6)

def menu():
    while True:
        print("""
        ======= BIENVENIDO A LA CALCULADORA CIENTÍFICA ========
        *******************************************************
        *                  1. Ingresar Datos                  *
        *                  2. Salir                           *
        *******************************************************
        """)
        opcion = int(input("Seleccione una Opcion: "))
        print()
        if opcion == 1:
            main()
        else:
            if opcion == 2:
                print(f"Gracias por Confiar en nosotros\n")
                break
            else:
                print("Dato errado la opcion solo puede ser 1 o 2")
menu()
    
