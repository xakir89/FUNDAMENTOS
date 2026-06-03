#dados n numeros almacenados en una lista mostrar el promedio de los pares e impares almacenados en la lista
#capturarn, Cacturar numeros, promediopar, promedioimpa, inicio
def capturarn():
    n=int(input("Ingrese cantidad de numeros que van a entrar a la lista:"))
    return n

def cacturarnumeros(n):
    lista=[]
    for i in range(0,n):
        x = int(input("digite un numero:"))
        lista.append(x)
    return lista
   
def promediopar(lista):
    acu = 0
    con =0
    for i in range(0,len(lista)):
        if lista[i]%2==0:
            acu += lista[i]
            con += 1
    if con > 0:
        pro = acu/con
        print("Promedio de los pares",pro)
    else:
        print("no hay impares en la lista")

def promedioimpar(lista):
    acu = 0
    con =0
    for i in range(0,len(lista)):
        if lista[i]%2 != 0:
            acu = acu + lista[i]
            con = con + 1
    if con > 0:
        pro = acu/con
        print("Promedio de los Impares",pro)
    else:
        print("no hay pares en la lista")

def STARD():
    n=capturarn()
    lista=cacturarnumeros(n)
    promediopar(lista)
    promedioimpar(lista)
STARD()



