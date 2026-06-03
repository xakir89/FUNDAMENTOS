###########################################################################################################
#                                   Condiciones de anidacion corregido por mi                             #
###########################################################################################################
print(f"ANIDADOS \n")

x = int(input("DIGITE UN VALOR DE 9 DIGITOS PARA EL INGRESO:"))
if 99999999 < x < 1000000000:
    he = x // 10000000
    hs = (x % 10000000) // 100000
    vvvv = (x//10)%10000
    s = x%10
    if he < 24:
        if hs < 24:
            if hs > he:
                ht = hs - he
                sueldo = ht * vvvv
                if 0 < s < 3:
                    if s ==1:
                        sm = sueldo * 1.10
                        print(f"\n El sueldo de esta persona de sexo Masculino es de: {sm} pesos")
                    else:
                        sf = sueldo * 1.20
                        print(f"\n El sueldo de esta persona de sexo Femenino es de: {sf} pesos")
                else:
                    print("Error, sexo solo puede ser 1 para hombre 2 para mujer")
            else:
                print("Error, hora salida tiene que ser mayor que hora de entrada")
        else:
            print("Error, Hora de entrada tiene que se menor que 24")            
    else:
        print("Error, Hora de entrada tiene que se menor que 24")
else:
    print("Error la entrada no puede ser menor que 9 digitos")

