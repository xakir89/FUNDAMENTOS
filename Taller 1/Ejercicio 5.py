print("\n Elaborar un algoritmo que tome como argumento tres números y retorne la suma de los cuadrados de estos números.\n")
a = int(input("Ingresa valor de a tres digitos:"))
if 99 < a < 1000:
    b = a // 100
    c = (a % 100) // 10
    d = a % 10
    sc = b**2+c**2+d**2
    print(f"\n Valor B: {b} \n Valor C: {c} \n Valor D: {d} \n \n Suma de sus Cuadrados: {sc}")
else:
    print(f"\n VALOR NO VALIDO DEBE SER 3 DIGITOS")
