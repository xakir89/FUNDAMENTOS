###########################################################################################################
# 11. Una empresa de telefonía alquila tarjetas para realizar llamadas y cobran el monto consumido        #
# de la tarjeta más un recargo del 20%. Teniendo como dato de entrada el monto inicial y el monto final   #
# de la tarjeta, elaborar un algoritmo para determinar el costo de la llama                               #
###########################################################################################################
print(f"TELEFONIA EL ANDY \n")
MONTOINICIAL = float(input("TOTAL CUPO TARJETRA:"))
MONTOFINAL = float(input("CONSUMO DE SU TARJETA:"))
CONSUMO = MONTOINICIAL - MONTOFINAL
RECARGO = CONSUMO *0.20
TOTALPAGO = CONSUMO + RECARGO

print(f"\n MONTO INICIAL: {MONTOINICIAL:.2f} PESOS \n MONTO FINAL: {MONTOFINAL:.2f} PESOS \n CONSUMO: {CONSUMO:.2f}  PESOS \n RECARGO: {RECARGO:.2f}  PESOS \n TOTAL PAGO:{TOTALPAGO:.2f}  PESOS\n \n GRACIAS POR USAR NUESTRA APP")
print(f"")

