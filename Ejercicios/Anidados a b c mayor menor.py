###########################################################################################################
#      Condiciones de anidacion a b c mostrar qe numero es mayor y que numero es menor sin que se repitan #
###########################################################################################################
print(f"ANIDADOS \n")

a = int(input("DIGITE UN Numero del 1 al 9"))
b = int(input("DIGITE UN Numero del 1 al 9:"))
c = int(input("DIGITE UN Numero del 1 al 9:"))
if a > b:
    if a > c:
        print(f"A es MAYOR \n")
        if b > c:
            print(f"C es Menor \n")
        else:
            print(f"B es Menor \n")
    else:
        print(f"C es MAYOR \n")
        print(f"B es Menor \n")
else:
    if b>c:
        print(f"B es MAYOR \n")
        if a>c:
            print(f"C es Menor \n")
        else:
            print(f"A es Menor \n")
    else:
        print(f"C es MAYOR \n")
        print(f"A es Menor \n")
