def tipoempleado():#aqui genero el tipo de empleado 
    print("Escoja tipo de empleado:\n")
    print("1 para Oficina OF\n2 para Operarios OP\n3 para Transporte TR\n")
    te = int(input("ingrese una opcion: "))
    while te <1 or te>3:
        te = int(input("\ningreso no valido.\n\n1 para Oficina OF\n2 para Operarios OP\n3 para Transporte TR\n\ningrese una opcion: "))
    if te==1:
        print("empleado de Oficina OF hora de ingreso 9:00 AM")
        tie= "Oficina"
    if te==2:
        print("empleado de Operarios OP hora de ingreso 7:30 AM")
        tie= "Operativo"
    if te==3:
        print("empleado de Transporte TR hora de ingreso 6:00 AM")
        tie= "Transporte"
    return tie
def creare():#aqui cree el empleado
    empleado=[]
    identificacion = int(input("INGRESE CC: "))
    nombre = input("INGRESE NOMBRES: ")
    apellido = input("INGRESE APELLIDOS: ")    
    edad = int(input("INGRESE edad: "))
    while edad < 16 or edad> 79:
        edad = int(input("Eda Invalida...\nINGRESE edad: "))
    tipo = tipoempleado()
    empleado.append(identificacion)     #[0]
    empleado.append(nombre)             #[1]
    empleado.append(apellido)           #[2]
    empleado.append(edad)               #[3]
    empleado.append(tipo)               #[4]
    empleado.append([])                 #[5] Vacia para fecha y hora de ingreso y estado
    empleado.append([])                 #[6] Vacia para fecha y hora de salida

    return empleado
def menu(): #genero la lista de lista y el menu principal
    empleados = []
    opc = 0
    while opc != 10:
        print("\nMENU\n")
        print("1. Crear Empleado")
        print("2. Registrar Ingreso")
        print("3. Mostrar Todos Los Ingresos")
        print("4. Mostrar Quienes Llegan Tarde")
        print("5. Mostrar Ingresos OF")
        print("6. Mostrar Ingresos OP")
        print("7.Mostar Ingreso TR")
        print("8. Visualizar Empleados")
        print("9. Registrar Salida")
        print("10. Salir\n")
        opc = int(input("ingrese una opcion: "))
        print()
        if opc == 1:
            ne = creare()
            empleados.append(ne)
            print("Empleado Creado Correctamente")
        if opc == 2:
            print("Registro de Ingreso:")
            registroentrada(empleados)
        if opc == 3:
            print("Mostrando Todos Los Registros:\n")
            for filas in range(0, len(empleados)):
                asistencias = empleados[filas][5] 
                salidas = empleados[filas][6]
                for i in range(0, len(asistencias)):
                    fecha_in = asistencias[i][0]
                    hora_in = asistencias[i][1]
                    estado_in = asistencias[i][2]
                    hora_out = "Sin Salida"
                    h_extra = "0H:00M"
                    for s in range(0, len(salidas)):
                        if salidas[s][0] == fecha_in:
                            hora_out = salidas[s][1]
                            h_extra = salidas[s][3]
                    print(f"CC: {empleados[filas][0]} | Nombre: {empleados[filas][1]} | Fecha: {fecha_in} | Entró: {hora_in} ({estado_in}) | Salió: {hora_out} | Extras: {h_extra}")          
                    
        if opc == 4:
            print("Llegadas Tarde:\n")
            for filas in range(0, len(empleados)):
                asistencias = empleados[filas][5]
                salidas = empleados[filas][6]
                for i in range(0, len(asistencias)):
                    if asistencias[i][2] == "Tarde":
                        fecha_in = asistencias[i][0]
                        hora_in = asistencias[i][1]
                        estado_in = asistencias[i][2]
                        hora_out = "Sin Salida"
                        h_extra = "0H:00M"
                        for s in range(0, len(salidas)):
                            if salidas[s][0] == fecha_in:
                                hora_out = salidas[s][1]
                                h_extra = salidas[s][3]                               
                        print(f"CC: {empleados[filas][0]} | Nombre: {empleados[filas][1]} | Fecha: {fecha_in} | Entró: {hora_in} ({estado_in}) | Salió: {hora_out} | Extras: {h_extra}")
                        
        if opc == 5:
            print("Mostrar Registros Empleados Oficina:\n")
            for filas in range(0, len(empleados)):
                if empleados[filas][4] == "Oficina":
                    asistencias = empleados[filas][5]
                    salidas = empleados[filas][6]
                    for i in range(0, len(asistencias)):
                        fecha_in = asistencias[i][0]
                        hora_in = asistencias[i][1]
                        estado_in = asistencias[i][2]
                        hora_out = "Sin Salida"
                        h_extra = "0H:00M"
                        for s in range(0, len(salidas)):
                            if salidas[s][0] == fecha_in:
                                hora_out = salidas[s][1]
                                h_extra = salidas[s][3]
                        print(f"CC: {empleados[filas][0]} | Nombre: {empleados[filas][1]} | Fecha: {fecha_in} | Entró: {hora_in} ({estado_in}) | Salió: {hora_out} | Extras: {h_extra}")
                        
        if opc == 6:
            print("Mostrar Registros Empleados Operadores:\n")
            for filas in range(0, len(empleados)):
                if empleados[filas][4] == "Operativo":
                    asistencias = empleados[filas][5]
                    salidas = empleados[filas][6]
                    for i in range(0, len(asistencias)):
                        fecha_in = asistencias[i][0]
                        hora_in = asistencias[i][1]
                        estado_in = asistencias[i][2]
                        hora_out = "Sin Salida"
                        h_extra = "0H:00M"
                        for s in range(0, len(salidas)):
                            if salidas[s][0] == fecha_in:
                                hora_out = salidas[s][1]
                                h_extra = salidas[s][3]
                        print(f"CC: {empleados[filas][0]} | Nombre: {empleados[filas][1]} | Fecha: {fecha_in} | Entró: {hora_in} ({estado_in}) | Salió: {hora_out} | Extras: {h_extra}")
                        
        if opc == 7:
            print("Mostrar Registros Empleados Transporte:\n")
            for filas in range(0, len(empleados)):
                if empleados[filas][4] == "Transporte":
                    asistencias = empleados[filas][5]
                    salidas = empleados[filas][6]
                    for i in range(0, len(asistencias)):
                        fecha_in = asistencias[i][0]
                        hora_in = asistencias[i][1]
                        estado_in = asistencias[i][2]
                        hora_out = "Sin Salida"
                        h_extra = "0H:00M"
                        for s in range(0, len(salidas)):
                            if salidas[s][0] == fecha_in:
                                hora_out = salidas[s][1]
                                h_extra = salidas[s][3]
                        print(f"CC: {empleados[filas][0]} | Nombre: {empleados[filas][1]} | Fecha: {fecha_in} | Entró: {hora_in} ({estado_in}) | Salió: {hora_out} | Extras: {h_extra}")
        if opc == 8:
            visualizar(empleados)
        if opc == 9:
            print("Registro de Salida:")
            registrosalida(empleados)            
        if opc == 10:
            print("Adios...")
        if opc <1 or opc > 10:
            print("Opcion Invalida...")

def visualizar(empleados):
    n = len(empleados)
    print("Identificacion  Nombre  Apelldido Edad Tipo\n")
    print("-" * 50)
    for filas in range(0,n):
        for columnas in range(0,6):
            print(empleados[filas][columnas],end="   ")
        print()

def registroentrada(empleados):
    if len(empleados) == 0:
        print("\nError: No hay empleados creados todavía. Vaya a la opción 1 primero.")
        return
    buscar_id = int(input("Ingrese La Identificacion del Empleado Que Va a Ingresar: "))
    empleado_actual = None
    for emp in empleados:
        if emp[0] == buscar_id:
            empleado_actual = emp
            break
    if empleado_actual == None:
        print("")
        return
    fecha = int(input("Ingrese la fecha en formato DDMMAAAA (ej: 04062026): "))
    dd = fecha // 1000000
    mm = (fecha // 10000) % 100
    anio = fecha % 10000
    while anio < 2026 or dd < 1 or dd > 31 or mm < 1 or mm > 12:
        print("\n[FECHA INVÁLIDA] Por favor verifique los datos\n")
        print(f"-> Día detectado: {dd} (Debe ser 1-31)")
        print(f"-> Mes detectado: {mm} (Debe ser 1-12)")
        print(f"-> Año detectado: {anio} (Debe ser 2026 en adelante)")
        fecha = int(input("Fecha Erronea.\nIngrese la fecha en formato DDMMAAAA (ej: 04062026): "))
        dd = fecha // 1000000
        mm = (fecha // 10000) % 100
        anio = fecha % 10000
    fecha_formateada = f"{dd}/{mm}/{anio}"
    asistencias = empleado_actual[5]                #valido que solo pueda entra una vez por dia
    for i in range(0, len(asistencias)):
        if asistencias[i][0] == fecha_formateada:
            print(f"\nError: Este empleado ya tiene un ingreso registrado para la fecha {fecha_formateada}.")
            return
    hora = int(input("Ingrese Hora de ingreso en formato 23/59: "))
    hr =  hora//100
    mt = hora % 100
    while hr < 0 or hr > 23 or mt < 0 or mt > 59:
        print("\n[HORA INVÁLIDA] Por favor verifique los datos\n")
        print(f"-> Hora detectado: {hr} (Debe ser 1-23 Horas)")
        print(f"-> Minutos detectado: {mt} (Debe ser 1-59 Minutos)")
        hora = int(input("hora Erronea\nIngreso permitido a partir de las 00:00 hasta las 23:59\nIngrese Hora de ingreso: "))
        hr = hora // 100
        mt = hora % 100
    tipo = empleado_actual[4] 
    estado_entrada = " - "
    if tipo == "Oficina":
        if hora == 900:
            estado_entrada = "A Tiempo"
        if hora < 900:
            estado_entrada = "Temprano"
        if hora >900:
            estado_entrada = "Tarde"
    if tipo == "Operativo":
        if hora == 730:
            estado_entrada = "A Tiempo"
        if hora < 730:
            estado_entrada = "Temprano"
        if hora > 730:
            estado_entrada = "Tarde"
    if tipo == "Transporte":
        if hora == 600:
            estado_entrada = "A Tiempo"
        if hora < 600:
            estado_entrada = "Temprano"
        if hora > 600:
            estado_entrada = "Tarde"
    hora_formateada = f"{hr}:{mt:02d}"
    
    nueva_asistencia = [fecha_formateada, hora_formateada, estado_entrada]
    empleado_actual[5].append(nueva_asistencia)
    print(f"Ingreso registrado con éxito! Estado: {estado_entrada}")
    return fecha_formateada, hora_formateada

def registrosalida(empleados):
    if len(empleados) == 0:
        print("\nError: No hay empleados creados todavía. Vaya a la opción 1 primero.")
        return
    buscar_id = int(input("Ingrese La Identificacion del Empleado Que Va a Ingresar: "))
    empleado_actual = None
    for emp in empleados:
        if emp[0] == buscar_id:
            empleado_actual = emp
            break
    if empleado_actual == None:
        print("")
        return
    horas = int(input("Ingrese Hora de ingreso en formato 23/59: "))
    hr =  horas//100
    mt = horas % 100
    while hr < 0 or hr > 23 or mt < 0 or mt > 59:
        print("\n[HORA INVÁLIDA] Por favor verifique los datos\n")
        print(f"-> Hora detectado: {hr} (Debe ser 1-23 Horas)")
        print(f"-> Minutos detectado: {mt} (Debe ser 1-59 Minutos)")
        horas = int(input("hora Erronea\nIngreso permitido a partir de las 00:00 hasta las 23:59\nIngrese Hora de ingreso"))
        hr = horas // 100
        mt = horas % 100
    tipo = empleado_actual[4] 
    estado_salida = horas
    min_reg_salida = 0

    # Logica de salida (8 horas despues de la entrada)
    if tipo == "Oficina":
        min_reg_salida = 1020 # 17:00 en minutos (17 * 60)
        if horas == 1700:
            estado_salida = "A Tiempo"
        if horas < 1700:
            estado_salida = "Salio Temprano"
        if horas > 1700:
            estado_salida = "Horas Extra"
            
    if tipo == "Operativo":
        min_reg_salida = 930 # 15:30 en minutos (15 * 60 + 30)
        if horas == 1530:
            estado_salida = "A Tiempo"
        if horas < 1530:
            estado_salida = "Salio Temprano"
        if horas > 1530:
            estado_salida = "Horas Extra"
            
    if tipo == "Transporte":
        min_reg_salida = 840 # 14:00 en minutos (14 * 60)
        if horas == 1400:
            estado_salida = "A Tiempo"
        if horas < 1400:
            estado_salida = "Salio Temprano"
        if horas > 1400:
            estado_salida = "Horas Extra"

    # Cálculo matemático de las Horas Extras exactas
    minutos_salida_real = (hr * 60) + mt
    minutos_extra = 0
    
    if minutos_salida_real > min_reg_salida:
        minutos_extra = minutos_salida_real - min_reg_salida
        
    he_horas = minutos_extra // 60
    he_mins = minutos_extra % 60
    horas_extras_str = f"{he_horas}H:{he_mins:02d}M"

    hora_formateada = f"{hr}:{mt:02d}"
    
    # Ahora la salida guarda 4 datos
    nueva_salida = [hora_formateada, estado_salida, horas_extras_str]
    empleado_actual[6].append(nueva_salida)
    
    print(f"Salida registrada con éxito! Estado: {estado_salida}")
    if minutos_extra > 0:
        print(f"Total horas extras realizadas hoy: {horas_extras_str}")


    print(f"Ingreso registrado con éxito! Estado: {estado_salida}")
    
menu()

    

