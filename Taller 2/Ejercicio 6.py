###################################################################################################
#   6. Elaborar un algoritmo que lea el nombre, la edad, el sexo y el estado civil de cualquier   #
#   persona e imprima el nombre de la persona; solo si, corresponde a un hombre casado,           #
#   mayor de 40 años o una mujer soltera menor de 50 años, y un mensaje que así lo indique.       #
###################################################################################################

nombre=str(input("INGRESE EL NOMBRE: "))
edad=int(input("INGRESE EDAD: "))
sexo=int(input("SEXO 1=MASCULINO 2=FEMENINO: "))
estado=int(input("ESTADO CIVIL 1=SOLTER@ - 2=CASAD@: "))



if 0 < sexo < 3:
    if 0 < estado < 3:
        if sexo==1:
            if estado==2:
                if edad>40:
                    print(f"\nNombre del pasiente: {nombre} \nEdad: {edad} \nEstado civil: Casado  ")
        else:
            if estado==1:
                if edad<50:
                    print(f"\nNombre del pasiente: {nombre} \nEdad: {edad} \nEstado civil: Soltera ")
    else:
        print("ESTADO CIVIL SOLO PUEDE SER 1=SOLTER@ o 2=CASAD@")    
else:
    print("SEXO SOLO PUEDE SER 1 PARA MASCULINO O 2 PARA FEMENINO")

    




