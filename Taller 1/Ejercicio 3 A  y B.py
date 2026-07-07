

def opcion():
    opc = int(input("Seleccione una Opcion: "))
    while opc < 1 or opc > 3:
        print("Dato errado la opcion solo puede ser 1, 2 o 3")
        opc = int(input("Seleccione una Opcion: "))
    return opc

def dolar_a_pesos():
    p = 3400.10
    dolar = float(input("Ingresa Cantidad de Dolares para su cambio: "))
    pesos = p * dolar
    return dolar, pesos

def pesos_a_dolar():
    pesos = float(input("Ingresa Cantidad de Pesos para su cambio: "))
    p = 3400.10
    dolar = pesos / p
    return pesos, dolar

def tablero():
    inicio_programa = True
    while inicio_programa:
        print (f"""
    ********** TU CONVERSOR DE CONFIANZA **********
    *                                             *
    *         1. CONVERSOR DE DOLAR A PESOS       *
    *         2. CONVERSOR DE PESOS A DOLARES     *
    *         3. SALIR                            *
    *                                             *
    ***********************************************
    """)
        opc = opcion()
        if opc ==1:
            dolar, pesos = dolar_a_pesos()
            print(f"""
    ****** TU CONVERSOR DE DOLAR A PESOS **********
    *                                             *
    *    Cantidad de Dolares: {dolar}                *
    *    Cambio a Pesos Colombianos: $ {pesos:.1f}   *
    *                                             *
    ***********************************************
    """)
        if opc == 2:
            pesos,dolar = pesos_a_dolar()
            print(f"""
    ****** TU CONVERSOR DE PESOS A DOLARES ****** 
    *                                           *
    *    Cantidad de pesos: $ {pesos}           *
    *    Cambio a Dolares Americanos: {dolar:.1f}     *
    *                                           *
    *********************************************
    """)
        if opc == 3:
            print("GRACIAS POR CONFIAR EN NOSOTROS")
            inicio_programa = False

            

tablero()
    
