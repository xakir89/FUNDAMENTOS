print("\n  Una institución educativa le paga a sus profesores $ 30000  la hora y le hace un /n descuento del 5% por concepto de ahorro. Elaborar un algoritmo /n para determinar el monto del descuento y el monto total a pagar. \n ")

HORAST = float(input("HORAS TARBAJADAS POR EL DOCENTE"))
SALARIO = HORAST * 30000
DESCUENTO = SALARIO * 0.05
TOTALPAGO = SALARIO - DESCUENTO

print(f"\n HORAS DE TRABAJO DOCENTE: {HORAST} HORAS \n DESCUENTO: {DESCUENTO} PESOS \n TOTAL A PAGAR: {TOTALPAGO} \n \n GRACIAS POR USAR NUESTRA APP")
print(f"")

