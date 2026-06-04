print("#############################################################################################")
print("#                                                                                           #")
print("#   Elabore un algoritmo que permita leer un número entero de 4 dígitos e indique si        #")
print("#   es capicua o no. (Un número es capicúa si se lee igual de izquierda a derecha o de      #")
print("#   derecha a izquierda, 1221, 2332….). Implemente una definición que reciba como           #")
print("#   argumento el número y retorne True si es capicúa o False en caso contrario.             #")
print("#                                                                                           #")
print("#############################################################################################\n")
def valor():
    x=int(input("Ingrese un número de 4 digitos: "))
    print()
    while x<1000 or x>9999:
        x=int(input("\nError en el ingreso.\n\nIngrese un número de 4 digitos: "))
        print()
    m=x//1000
    c=(x%1000)//100
    d=(x%100)//10
    u=x%10
    return m, c, d, u, x
def capicua():
    m,c,d,u,x=valor()
    no_capicua=False
    while no_capicua ==False:     
        if m == u and c==d:
            print("el valor ingresado es Capicua",x,"\n" )
            no_capicua=True
        else:
            print("No es Capicua Vuelva a Ingresar\n ")
            m,c,d,u,x=valor()
            if m == u and c==d:
                print("el valor ingresado es Capicua",x,"\n" )
                no_capicua=True
            

capic 