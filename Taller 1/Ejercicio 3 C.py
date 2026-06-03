print (f"TU CONVERSOR DE CONFIANZA\n OPCION 1 CONVERSOR DE Grados centígrados a Farenheit \n OPCION 2 CONVERSOR DE Grados Farenheit a centígrados \n")
opcion = int(input(f"Seleccione una Opcion (1 o 2):"))

if  0 < opcion < 3:
    if opcion == 1:
        GC = float(input(f"Ingrese el Valor de Los Grados centrigrados:"))
        GF = GC*((9/5)+32)
        print (f"\n Teniendo en Cuenta los Grados Centigrados: {GC} \n Los Grados Farenheit Serian: {GF}\n")
    else:
        GFF = float(input(f"Ingrese el valor de Grados Farenmheit: \n"))
        GCC = (GFF-32)*(5/9)
        print(f"\n Teniendo en Cuenta los Grados Farenheit: {GFF} \n Los Grados Centigrados Serian: {GCC:.2f}")
else:
    print("OPCION NO VALIDA")
