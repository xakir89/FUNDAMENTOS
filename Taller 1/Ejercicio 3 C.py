# 3. Elaborar un algoritmo para cada uno de los siguientes problemas : 
#    a. Convertir de dólares a pesos 
#    b. Convertir de pesos a dólares 
#    c. Convertir de grados centígrados a Farenheit. 
#    d. Calcular el promedio de 3 números  

def ingreso(dato):
    x = int(input(F"Ingrese Dato Solicitado {dato}: "))
    print()
    return x

def ingresoG(dato):
    x = float(input(F"Ingrese Dato Solicitado {dato}: "))
    print()
    return x

def opc ():
    
    bandera = True
    while bandera:
        Tablero()
        opc = ingreso("opcion")
        if opc == 1:
            gc = ingresoG("Grados Centigrados")
            gf = (gc*(9/5))+32
            print(f"""
++++++++++++++++++++++++++++++++++++++++++++++
+                                            +
+           Grados centigrados {gc}          +
+              convertidos                   +
+           Grados Farenheit {gf:.1f}            +
+                                            +
++++++++++++++++++++++++++++++++++++++++++++++
""")
        elif opc == 2:
            gf = ingresoG(f"Grados Farenheit")
            gc = (gf-32)*(5/9)
            print(f"""
++++++++++++++++++++++++++++++++++++++++++++++
+                                            +
+           Grados Farenheit {gf}            +
+               convertidos                  +
+           Grados centigrados {gc:.1f}          +
+                                            +
++++++++++++++++++++++++++++++++++++++++++++++
    """)
        elif opc == 3:
            print("Gracias por Confiar en nosotros")
            print()
            bandera = False
        else:
            print(f"Dato Errado solo hay 3 opciones Disponibles\n")

                    
def Tablero():
    print (f"""
+++++++++++++++++++++++++++++++++++++++++++++
+                                           +
+        TU CONVERSOR DE CONFIANZA          +
+                                           +
+    1. Grados centígrados a Farenheit      +
+    2. Grados Farenheit a centígrados      +
+    3. SALIR                               +
+                                           +
+++++++++++++++++++++++++++++++++++++++++++++
""")
opc()
    

