def variable(v):
    x = float(input(f"Ingrese el valor para {v}: "))
    print()
    return x
def area_triangulo():
    base = variable("base del triangulo")
    altura = variable("altura del triangulo")
    area = (base*altura)/2
    return area
def area_rombo():
    diagional_mayor = variable("diagonal mayor del rombo")
    diagonal_menor = variable("diagonal menor del rombo")
    area = (diagional_mayor*diagonal_menor)/2
    return area
def area_trapesio():
    base_mayor = variable("base mayor del trapesio")
    base_menor = variable("base menor del trapesio")
    altura = variable("altura del trapesio")
    area = ((base_mayor+base_menor)*altura)/2
    return area



def menu():
    while True:
        print("""
        ************ BIENVENIDO AL ALGORITMO DE AREAS ************
        *                                                        *
        *                1. hallar Area Triangulo                *
        *                2. hallar Area Rombo                    *
        *                3. hallar Area Trapesio                 *
        *                4. Salir                                *    
        *                                                        *
        **********************************************************
        """)
        opc = int(input("Seleccione una Opcion: "))
        if opc == 1:
            area = area_triangulo()
            print(f"""
        ******************* AREA DEL TRIANGULO *******************
        *       *                                                *
        *      * *          BASE  X ALTURA                       *
        *     *   *        ---------------- = {area:.2f}          *
        *    *******               2                             *
        *                                                        *
        **********************************************************
        """)            
        elif opc == 2:
            area = area_rombo()
            print(f"""
        ********************* AREA DEL ROMBO *********************
        *  ***********                                           *
        *   *         *    DIAGONAL MAYOR  X DIAGONAL MENOR      *
        *    *         *   ---------------------------------     *
        *     ***********             2                          *
        *                                        = {area:.2f}    *
        **********************************************************
        """)   
        elif opc == 3:
            area = area_trapesio()
            print(f"""
        ******************** AREA DEL TRAPESIO *******************
        *      ****                                              *
        *     *    *          (BASE MAYOR + BASE MENOR) X ALTURA *
        *    *      *        ----------------------------------- *
        *    *********                       2                   *
        *                                       = {area:.2f}     *
        **********************************************************
        """)   
        elif opc == 4:
            print("Gracias por confiar en nosotros")
            print()
            break
        else:
            print("Dato errado la opcion solo puede ser 1 al 4")
menu()



