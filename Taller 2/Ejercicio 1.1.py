def validarnota(numero_nota):
    bandera = True
    while bandera:
        print(f"Registro Notas Estudiante {estuNo}")
        nota = float(input("Ingrese Nota {nota}: "))
        if nota >= 0 and nota <=5:
                bandera = False
                return nota
        else:
            print("La nota debe ser de 0.0 a 5.0")         
            
def estudiante(numero_estudiante):
    print(f"\n--- Registro Estudiante {numero_estudiante} ---") 
    nombre = input("Ingrese Nombre del estudiante: ")

    n1 = validarnota(1)
    n2 = validarnota(2)
    n3 = validarnota(3)
    n4 = validarnota(4)

    pro = (n1+n2+n3+n4) / 4

    return [nombre, n1, n2, n3, n4, pro]
def menu():
    print("""
******************************************
*                                        *
*      ingreso de Notas Estudiantes      *
*                                        *
*      1. ingreso notas Estudiantes      *
*      2. consultar Estudiantes          *
*      3. Ganador beca                   *
*      4. Salida                         *
*                                        *
******************************************
""")
    bandera = True
    while bandera:
        opc = int(input("Ingresa una Opcion: "))
        if opc == 1:
            estudiante(numero_estudiante)

def final():
    columna = [Nombre, Nota_1, Nota_2, Nota_3, Nota_4]
    fila = []
    
if 0 <= e1n1 <= 5:
    if 0 <= e1n2 <= 5:
        if 0 <= e1n3 <= 5:
            if 0 <= e1n4 <= 5:
                promedio1 = (e1n1 + e1n2 + e1n3 + e1n4) / 4
                
                # --- DATOS ESTUDIANTE 2 ---
                print("\n--- Registro Estudiante 2 ---")
                e2n1 = float(input("Ingrese Nota 1: "))
                e2n2 = float(input("Ingrese Nota 2: "))
                e2n3 = float(input("Ingrese Nota 3: "))
                e2n4 = float(input("Ingrese Nota 4: "))
                
                if 0 <= e2n1 <= 5:
                    if 0 <= e2n2 <= 5:
                        if 0 <= e2n3 <= 5:
                            if 0 <= e2n4 <= 5:
                                promedio2 = (e2n1 + e2n2 + e2n3 + e2n4) / 4
                                
                                # --- LÓGICA DE LA BECA ---
                                print(f"\nPromedios: E1: {promedio1} | E2: {promedio2}")
                                
                                # Caso 1: Estudiante 1 tiene mejor promedio y califica
                                if promedio1 > 4.5:
                                    if promedio1 > promedio2:
                                        print("Resultado: El estudiante 1 es el ganador de la beca.")
                                
                                # Caso 2: Estudiante 2 tiene mejor promedio y califica
                                if promedio2 > 4.5:
                                    if promedio2 > promedio1:
                                        print("Resultado: El estudiante 2 es el ganador de la beca.")
                                
                                # Caso 3: Empate por encima de 4.5
                                if promedio1 > 4.5:
                                    if promedio1 == promedio2:
                                        print("Resultado: Ambos estudiantes ganaron la beca.")
                                
                                # Caso 4: Nadie llega al 4.5
                                if promedio1 <= 4.5:
                                    if promedio2 <= 4.5:
                                        print("Resultado: Ninguno de los dos estudiantes ganó la beca.")
                                        
                            else: print("Error: Nota del E2 fuera de rango (0-5).")
                        else: print("Error: Nota del E2 fuera de rango (0-5).")
                    else: print("Error: Nota del E2 fuera de rango (0-5).")
                else: print("Error: Nota del E2 fuera de rango (0-5).")
            else: print("Error: Nota del E1 fuera de rango (0-5).")
        else: print("Error: Nota del E1 fuera de rango (0-5).")
    else: print("Error: Nota del E1 fuera de rango (0-5).")
else: print("Error: Nota del E1 fuera de rango (0-5).")
