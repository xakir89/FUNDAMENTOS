def menu():
    print("...........Cine Colombia...........")
    print("")
    print("1. Valor Silla\n1. General\n2. VIP\n3. Mostrar Valores")
    print("4. Visualizar")
    print("5. Buscar Factura")
    print("6. Cuadre Caja")
    print("7. Salir")
    print("")
    opc=0
    while opc !=7:
        opc=int(input("Ingrese una Opcion "))
        if opc == 1:
            valorsilla()
        if opc == 2:
            print("2. VIP")
        if opc == 3:
            print("3. Mostrar Valores")
        if opc == 4:
            print("4. Visualizar")
        if opc == 5:
            print("5. Buscar Factura")
        if opc == 6:
            print("6. Cuadre de Caja")
        if opc == 7:
            print("Salir...")
            
def valorsilla():
    valorsillas = [5000,10000,"General: $ 5.000 VIP: 10.000"]
    print("")
    print("1. General ")
    print("2. VIP ")
    print("3. Mostrar Valores ")
    opc=0
    ge=0
    vip=0
    while opc != 4:
        opc=int(input("Ingrese una Opcion "))
        if opc==1:
            print("General Costo $ 5.000:")
        if opc==2:
            print("VIP Costo $ 10.000:")
        if opc==3:
            print("Mostrar Valores:")
        if opc==4:
            print("Volver")

def sillas():
    st = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14]]
    filas = len(st)
    col = 5
    for filas in range(0,filas):
        for col in range(0,col):
            print(st[col],end="")
            print("")
menu()

