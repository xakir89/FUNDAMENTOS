def menu():
    histaorial_facturas = []
    numero_factura = 1

    sillas=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    opc=0
    while opc != 7:
        print("\n........... Cine Colombia ...........\n")
        print("1. Consultar Precios (General y VIP)")
        print("2. Comprar Silla")
        print("3. Visualizar Sillas Disponibles")
        print("4. Buscar Factura")
        print("5. Cuadre de Caja")
        print("7. Salir\n")
        print(".....................................")

        opc=int(input("\nIngrese una Opcion: "))
        if opc == 1:
            print("")
            valorsilla()
        if opc == 2:
            print("2. ")
            numero_factura = comprarsillas(sillas, numero_factura, histaorial_facturas)
        if opc == 3:
            print("\n........... Visualizacion Sillas Disponibles ...........\n")
            mostrarsillas(sillas)
        if opc == 4:
            print("\n........... Buscar Factura ...........\n")
            buscar_factura(histaorial_facturas)
        if opc == 5:
            print("\n........... Cuadre de Caja ...........\n")
            cuadre_caja(histaorial_facturas)
        if opc == 7:
            print("\nSaliendo del Sistemas...\n")

def valorsilla():
    print("\n--- Valores de Sillas ---\n")
    print("General: $ 5.000")
    print("VIP: $ 10.000\n")
    print("-------------------------")
            
def comprarsillas(sillas, numero_factura, historial_factura):
    # Variables locales para acumular la compra actual del cliente
    cant_general = 0
    cant_vip = 0
    total_compra = 0

    print("\n--- INICIO DE COMPRA ---")

    while True:
        desea_general = input("\n¿Desea silla General? (s/n): ")
        if desea_general == "s" or desea_general == "n" or desea_general == "S" or desea_general == "N":
            break
        else:
            print("\n¡ERROR! Ingrese 's' para sí o 'n' para no.")
    # 1. Selección Iterativa de Sillas Generales
    while desea_general == "s" or desea_general == "S":
        mostrarsillas(sillas)
        pos = int(input("\nDigite el número de silla General (0-9): "))
    desea_general = input("\n¿Desea silla General? (s/n): ")
    while desea_general == "s" or desea_vip == "S":    
        if rango(pos) and pos <= 9:
            if sillas[pos] == "X":
                print("\n¡ERROR! Silla ocupada")
            else:
                sillas[pos] = "X"
                cant_general = cant_general + 1
                total_compra = total_compra + 5000
                print(f"\nSilla General {pos} agregada exitosamente.")
        else:
            print("\n¡ERROR! El número ingresado no corresponde a la zona General.")

        desea_general = input("\n¿Desea otra silla General? (s/n): ")

    # 2. Selección Iterativa de Sillas VIP
    while True:
        desea_vip = input("\n¿Desea silla VIP? (s/n): ")
        if desea_vip == "s" or desea_vip == "n" or desea_vip == "S" or desea_vip == "N":
            break
        else:
            print("\n¡ERROR! Ingrese 's' para sí o 'n' para no.")
            
    desea_vip = input("\n¿Desea silla VIP? (s/n): ")
    while desea_vip == "s" or desea_vip == "S":
        mostrarsillas(sillas)
        pos = int(input("\nDigite el número de silla VIP (10-19): "))
        
        if rango(pos) and pos >= 10:
            if sillas[pos] == "X":
                print("¡ERROR! Silla ocupada")
            else:
                sillas[pos] = "X"
                cant_vip = cant_vip + 1
                total_compra = total_compra + 10000
                print(f"Silla VIP {pos} agregada exitosamente.")
        else:
            print("\n¡ERROR! El número ingresado no corresponde a la zona VIP.")

        desea_vip = input("\n¿Desea otra silla VIP? (s/n): ")

    # 3. Procesamiento y registro final de la Factura Unificada
    if cant_general > 0 or cant_vip > 0:
        nombre_cliente = input("\nDigite el nombre del cliente: ")
        
        # Guardamos el registro consolidado en la matriz de historial
        nueva_fila = [numero_factura, nombre_cliente, cant_general, cant_vip, total_compra]
        historial_ura = historial_factura.append(nueva_fila)
        
        print("\n ¡COMPRA REALIZADA CON EXITO! Factura No. ", numero_factura)
        numero_factura = numero_factura + 1
    else:
        print("\n[!] No se seleccionó ninguna silla. No se generó la factura.")

    return numero_factura

def buscar_factura(historial_factura):
    if len(historial_factura) == 0:
        print("\n[!] No se han registrado ventas en el sistema.\n")
        return
    buscar_id = int(input("\nIngrese el número de factura a buscar: "))
    encontrada = False
    for i in range(len(historial_factura)):
        if historial_factura[i][0] == buscar_id:
            id_fac = historial_factura[i][0]
            cliente = historial_factura[i][1]
            c_gen = historial_factura[i][2]
            c_vip = historial_factura[i][3]
            total = historial_factura[i][4]

            total__general = c_gen * 5000
            total_vip = c_vip * 10000

            print("\n............... Factura Encontrada ...............\n")
            print("Factura No:", id_fac)
            print("Nombre del Cliente:", cliente)
            print("Sillas General Compradas:", c_gen)
            print("Sillas VIP Compradas:", c_vip)
            print("Total General: $", total__general)
            print("Total VIP: $", total_vip)
            print("Total a Pagar: $", total)
            encontrada = True
            break
    if encontrada == False:
        print("\n[X] No se encontró una factura con el número ingresado.\n")

def cuadre_caja(historial_factura):
    print("\n............... Cuadre de Caja ...............\n")
    if len(historial_factura) == 0:
        print("Ingresos Totales: $ 0")
        print("Cantidad de Sillas Vendidas: 0")
        print("Cantidad de Sillas Generales Vendidas: 0")
        print("Cantidad de Sillas VIP Vendidas: 0")
        return
    total_recaudado = 0
    cantidad_general = 0
    cantidad_vip = 0
    for i in range(len(historial_factura)):
        c_gen = historial_factura[i][2]
        c_vip = historial_factura[i][3]
        valor_total_factura = historial_factura[i][4]
        
        total_recaudado = total_recaudado + valor_total_factura
        cantidad_general = cantidad_general + c_gen
        cantidad_vip = cantidad_vip + c_vip
        
    print("Total Facturas Emitidas: ", len(historial_factura))
    print("Sillas Generales Vendidas: ", cantidad_general, f"($ {cantidad_general * 5000})")
    print("Sillas VIP Vendidas: ", cantidad_vip, f"($ {cantidad_vip * 10000})")
    print("Ingreso Total a Caja: $", total_recaudado)

def mostrarsillas(sillas):
    print("\n.........GENERAL.........\n")
    print("\n",sillas[0],"  |",sillas[1]," |",sillas[2]," |",sillas[3]," |",sillas[4]," |","\n")
    print("\n",sillas[5],"  |",sillas[6]," |",sillas[7]," |",sillas[8]," |",sillas[9]," |","\n")
    print("\n...........VIP...........\n")
    print("\n",sillas[10]," |",sillas[11],"|",sillas[12],"|",sillas[13],"|",sillas[14],"|","\n")
    print("\n",sillas[15]," |",sillas[16],"|",sillas[17],"|",sillas[18],"|",sillas[19],"|","\n")
    print("\n.........................\n")

def rango(pos):
    r=False
    if pos >= 0 and pos <=19:
        r=True
    return r

menu()
