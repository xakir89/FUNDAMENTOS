# Variables iniciales
total_iteraciones = 90  # 9 tablas x 10 números cada una
contador_operaciones = 0
tabla_actual = 1
multiplicador = 1

print(f"--- TABLA DEL {tabla_actual} ---")

# Un único ciclo for que avanza de 1 en 1
for i in range(1, total_iteraciones + 1):
    resultado = tabla_actual * multiplicador
    print(f"{tabla_actual} x {multiplicador} = {resultado}")
    
    # Contador y acumulador lógico
    contador_operaciones = contador_operaciones + 1
    
    # Lógica de control con IF para cambiar de tabla
    # Si el multiplicador llega a 10, reiniciamos y saltamos de tabla
    if multiplicador == 10:
        multiplicador = 1
        tabla_actual = tabla_actual + 1
        
        # Bandera lógica: ¿Aún quedan tablas por imprimir?
        continuar = tabla_actual <= 9
        
        if continuar:
            print(f"\n--- TABLA DEL {tabla_actual} ---")
    else:
        # Si no ha llegado a 10, solo sumamos 1 al multiplicador
        multiplicador = multiplicador + 1

# Verificación final con acumulador
if contador_operaciones == 90:
    print("\nProceso finalizado: Se imprimieron las 9 tablas correctamente.")
