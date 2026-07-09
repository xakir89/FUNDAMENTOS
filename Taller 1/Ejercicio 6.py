# Elaborar un algoritmo para calcular el IVA (16%) de un valor ingresado por teclado. 
# Ejemplo: valor digitado => 2000
# Mostrar en pantalla IVA = 320 y valor mas IVA = 2320.

def  
 
print("\n Elaborar un algoritmo para calcular el IVA (16%) de un valor ingresado por teclado. \n Ejemplo: valor digitado => 2000 Mostrar en pantalla IVA = 320 y valor mas IVA = 2320 \n")
PRECIO = float(input("PRECIO ARTICULO:"))

if PRECIO >= 2000:
    IVA = PRECIO * 0.16
    TOTAL = PRECIO + IVA
    print(f"\n VALOR ARTICULO: {PRECIO}\n VALOR IVA: {IVA} \n TOTAL A PAGAR: {TOTAL}\n \n GRACIAS POR SU COMPRA")
else:
    print(f"EL VALOR INGRESADO DEVE SER DE 2000 PESOS EN ADELANTE")
