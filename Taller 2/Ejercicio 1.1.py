# --- DATOS ESTUDIANTE 1 ---
print("--- Registro Estudiante 1 ---")
e1n1 = float(input("Ingrese Nota 1: "))
e1n2 = float(input("Ingrese Nota 2: "))
e1n3 = float(input("Ingrese Nota 3: "))
e1n4 = float(input("Ingrese Nota 4: "))

# Validación Matemática: 0 debe ser menor o igual a la nota
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
