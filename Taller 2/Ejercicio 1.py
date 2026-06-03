#   1. Elaborar un algoritmo que permita determinar cuál es el ganador de la beca de entre dos
#   estudiantes. El algoritmo deberá hallar la nota definitiva de cada uno de ellos (4 materias,
#   ingrese sus notas y calcule el promedio) Si es mayor que 4.5 el alumno podrá aspirar a la
#   beca, de lo contrario no.

e1n1=float(input("Ingrese Nota 1 del estudiante 1:"))
e1n2=float(input("Ingrese Nota 1 del estudiante 2:"))
e1n3=float(input("Ingrese Nota 1 del estudiante 3:"))
e1n4=float(input("Ingrese Nota 1 del estudiante 4:"))

if 0 <= e1n1 <= 5:
    if 0 <= e1n2 <= 5:
        if 0 <= e1n3 <= 5:
            if 0 <= e1n4 <= 5:
                promedioe1 = (e1n1 + e1n2 + e1n3 + e1n4)/4
                
                e2n1=float(input("Ingrese Nota 2 del estudiante 1:"))
                e2n2=float(input("Ingrese Nota 2 del estudiante 2:"))
                e2n3=float(input("Ingrese Nota 2 del estudiante 3:"))
                e2n4=float(input("Ingrese Nota 2 del estudiante 4:"))
                if 0 <= e2n1 <= 5:
                    if 0 <= e2n2 <= 5:
                        if 0 <= e2n3 <= 5:
                            if 0 <= e2n4 <= 5:
                                promedioe2 = (e2n1 + e2n2 + e2n3 + e2n4)/4
                                if promedioe1 > 4.5:
                                    if promedioe1 > promedioe2:
                                        print("el estudiante 1 es el ganador de la beca")
                                    else:
                                        if promedioe1 == promedioe2:
                                            print("Ambos estudiantes ganaron la beca")                                        
                                        else:
                                            print("Estudiante 2 es el ganador de la beca")
                                else:
                                    if promedioe2 > 4.5:
                                        print("El estudiante dos es ganador de la Beca")
                                    else:
                                        print("Ninguno de los dos estudiantes gano la beca")
                            else:
                                print("Nota fuera del Rago debe ser mayor de 0 y menor de 6")
                        else:
                            print("Nota fuera del Rago debe ser mayor de 0 y menor de 6")

                    else:
                        print("Nota fuera del Rago debe ser mayor de 0 y menor de 6")

                else:
                    print("Nota fuera del Rago debe ser mayor de 0 y menor de 6")
            else:
                print("Nota fuera del Rago debe ser mayor de 0 y menor de 6")
        else:
            print("Nota fuera del Rago debe ser mayor de 0 y menor de 6")
    else:
        print("Nota fuera del Rago debe ser mayor de 0 y menor de 6")
else:
    print("Nota fuera del Rago debe ser mayor de 0 y menor de 6")
