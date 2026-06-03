####################################################################################################
#                                                                                                  #
#       2. Elaborar un algoritmo que determine si un año ingresado por teclado es o no bisiesto    #
#                           (formato del dato de entrada yyyymmdd).                                #
#                                                                                                  #
####################################################################################################

fecha = int(input("Ingrese la Fecha en este formato AAAAMMDD:"))
if 9999999 < fecha < 1000000000:
    anio = fecha // 10000
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                print(f"\n este Año {anio} si es bisiesto ya que es \n divicible por 4 tambien es divisible por 100 y por 400")
        else:
            print(f"\n este Año {anio} si es bisiesto ya que es divicible por 4 y no es divisible por 100")
    else:
        print(f"\n este Año {anio} no es bisiesto ya que no es divicible por 4")
else:
    print(f"\n La fecha solo se puede ingresar 8 numeros en formato AAAAMMDD")
