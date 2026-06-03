print (f"TU CONVERSOR DE CONFIANZA \n \n OPCION 1 CONVERSOR DE DOLAR A PESOS \n OPCION 2 CONVERSOR DE PESOS A DOLARES \n")
opcion = int(input("Seleccione una Opcion (1 o 2):"))
DolarDia = 3687.10
if  0<opcion<3:
    if opcion==1:
        DOLARES = float(input("Ingrese cantidad de Dolares para su cambio:"))
        P = DOLARES*DolarDia
        print (f"\n Sus Dolares: {DOLARES} A Pesos es:{P} \n")
    else:
        PESOS = float(input(f"Ingrese cantidad de Pesos para su cambio:"))
        D = PESOS/DolarDia
        print(f"\n sus Pesos {PESOS} a Dolares son:{D:.2f}")
else:
    print("OPCION NO VALIDA")
