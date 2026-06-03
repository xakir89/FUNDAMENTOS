
## menu
## 1. crea usuarios (cod,nombre,edad, sexo, pago)
## 2. visualizar usuarios
## 3. modificar usuario
## 4. promedio de pago segun sexo (f o m)
## 5. salir
def promedio(usuarios,sexo):
    n = len(usuarios)
    acu = 0
    con = 0
    for filas in range(0,n):
        if usuarios[filas][3]==sexo:
            con = con + 1
            acu = acu + usuarios[filas][4]
    if con > 0:
        prom= acu / con
        print("el promedio del sexo=",sexo,"es",prom)
    else:
        print("no hay registrado el sexo = ",sexo)
        
def modificar(usuarios):
    cod = int(input("digite el código:"))
    n = len(usuarios)
    for filas in range(0,n):
        if usuarios[filas][0]==cod:
            nombre = input("digite el nombre:")
            edad = int(input("digite la edad:"))
            sexo = input("ingrese f o m:")
            pago = float(input("ingrese el pago:"))
            usuarios[filas][1]=nombre
            usuarios[filas][2]=edad
            usuarios[filas][3]=sexo
            usuarios[filas][4]=pago
    return usuarios

def visualizar(usuarios):
    n = len(usuarios)
    print("cod  nombre  edad   sexo  pago")
    for filas in range(0,n):
        for col in range(0,5):
            print(usuarios[filas][col],end="   ")
        print()
    
def crearusuario(cod):
    usuario = []
    nombre = input("digite el nombre:")
    edad = int(input("digite la edad:"))
    sexo = input("ingrese f o m:")
    pago = float(input("ingrese el pago:"))
    usuario.append(cod)
    usuario.append(nombre)
    usuario.append(edad)
    usuario.append(sexo)
    usuario.append(pago)
    return usuario
def menu():
    opc = 1
    cod = 2000
    usuarios =[]
    while opc>0 and opc < 5:
        print("menu")
        print("1. crea usuarios (cod,nombre,edad, sexo, pago)")
        print("2. visualizar usuarios")
        print("3. modificar usuario")
        print("4. promedio de pago segun sexo (f o m)")
        print("5. salir")
        opc = int(input("digite una opciòn:"))
        if opc==1:
            u = crearusuario(cod)
            usuarios.append(u)
            cod = cod + 1
        if opc == 2:
            visualizar(usuarios)
        if opc==3:
            usuarios = modificar(usuarios)
        if opc==4:
            sexo = input("digite el sexo f o m:")
            promedio(usuarios,sexo)
menu()
    
