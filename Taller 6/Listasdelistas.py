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
    tipo = tipoempleado()
    empleado.append(identificacion)
    empleado.append(nombre)
    empleado.append(apellido)
    empleado.append(edad)
    empleado.append(tipo)
    empleado.append("sin registrar")
    empleado.append("sin registrar")
    empleado.append("sin registrar")
    return empleado, identificacion
def menu(): #genero la lista de lista y el menu principal
    empleados = []
    ingreso = []
    opc = 0
    while opc != 9:
        print("\nMENU\n")
        print("1. Crear Empleado")
        print("2. Registrar Ingreso")
        print("3. Mostrar Todos Los Ingresos")
        print("4. Mostrar Quienes Llegan Tarde")
        print("5. Mostrar Ingresos OF")
        print("6. Mostrar Ingresos OP")
        print("7.Mostar Ingreso TR")
        print("8. Visualizar Empleados")
        print("9. Salir\n")
        opc = int(input("ingrese una opcion: "))
        print()
        if len(empleados) == 0:
            print("\nError: No hay empleados creados todavía. Vaya a la opción 1 primero.\n")
        if opc == 1:
            ne = creare()
            empleados.append(ne)
            print("Empleado Creado Correctamente")
        if opc == 2:
            print("Registro de Ingreso:")
            registroentrada(empleados,ingresos)
        if opc == 3:
            print("Mostrando Todos Los Ingresos:")
        if opc == 4:
            print("Llegadas Tarde:")
        if opc == 5:
            print("Mostrar Ingreso Empleados Oficina:")
        if opc == 6:
            print("Mostrar Ingreso Empleados Operadores:")
        if opc == 7:
            print("Mostrar Ingreso Empleados Transporte:")
        if opc == 8:
            visualizar(empleados)
        if opc == 9:
            print("Adios...")

def visualizar(empleados):
    n = len(empleados)
    print("Identificacion  Nombre  Apelldido Edad Tipo FechaIngreso HoraIngreso Entrada\n")
    for filas in range(0,n):
        for col in range(0,5):
            print(empleados[filas][col],end="   ")
        print()

def registroentrada(empleados):
    if len(empleados) == 0:
        print("\nError: No hay empleados creados todavía. Vaya a la opción 1 primero.")
        return
    buscar_id = int(input("Ingrese La Identificacion del Empleado Que Va a Ingresar: "))
    empleado_atual = None
    for emp in empleados:
        if emp[0] == buscar_id:
            empleado_actual = emp
            break
    if empleado_actual == None:
        print("")
        return
    fecha = int(input("Ingrese la Fecha en Formato DDMMAAAA"))
    


    hora = int(input("Ingrese Hora de ingreso"))
    while hora < 730 or hora > 2400:
        hora = int(input("hora Fuera del rango\nIngreso permitido a partir de las 07:30 hasta las 23:59\nIngrese Hora de ingreso"))
        if hora == 730 and 2359:
            print()

menu()

    

