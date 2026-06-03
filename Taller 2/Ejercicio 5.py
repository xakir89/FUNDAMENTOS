############################################################################################
#                                                                                          #
#   5. Elaborar un algoritmo que lea cuatro números ingresados por el usuario y los sume,  #
#   descartando los negativos.                                                             #
#                                                                                          #
############################################################################################


# 1. Entrada de datos
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el primer número: "))
c = int(input("Ingresa el primer número: "))
d = int(input("Ingresa el primer número: "))

if a>0:
    if b>0:
        if c>0:
            if d >0:
                x=a+b+c+d
                print(f"a = {a}, b = {b}, c = {c} y d = {d} son positivos y su suma es= {x}")
            else:
                x= a+b+c
                print(f"a = {a}, b = {b} y c = {c} son positivos y su suma es= {x}")
        else:
            if d > 0:
                x=a+b+d
                print(f"a = {a}, b = {b} y d = {d} son positivos y su suma es= {x}")
            else:
                x= a+b
                print(f"a = {a} y b = {b} son positivos y su suma es= {x}")
    else:
        if c>0:
            if d>0:
                x=a+c+d
                print(f"a = {a}, c = {c} y d = {d} son positivos y su suma es= {x}")
            else:
                x=a+c
                print(f"a = {a} y c = {c} son positivos y su suma es= {x}")
        else:
            if d>0:
                x=a+d
                print(f"a = {a} y d = {d} son positivos y su suma es= {x}")
            else:
                print(f"a es positivo = {a}")
else:
    if b>0:
        if c>0:
            if d>0:
                x=b+c+d
                print(f"b = {b}, c = {c} y d = {d} son positivos y su suma es= {x}")
            else:
                x=b+c
                print(f"b = {b} y c = {c} son positivos y su suma es= {x}")
        else:
            if d >0:
                x=b+d
                print(f"b = {b} y d = {d} son positivos y su suma es= {x}")
            else:
                print(f"b es positivo = {b}")
    else:
        if c>0:
            if d>0:
                x = c+d
                print(f"c = {c} y d = {d} son positivos y su suma es = {x}")
            else:
                print(f"c es positivo = {c}")
        else:
            if d > 0:
                print(f"d es positivo = {d}")
            else:
                print("todos los numeros son negativos y no se suman por lo tanto")
