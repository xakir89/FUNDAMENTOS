#numeros=[1,"anda",3,4,5,7]

#dados n Numeros Almacenados en una lista mostrar los numeros pares almacenados en la lista

#for i in range(0,n):
    #print (numeros[i])
n = int(input("Ingrese Longitud para la Lista:"))
lista=[]

def Crearlista (n)
    for i in range(1,n+1):
        x = int(input("digite un numero:"))
        lista.append(x)
    print(lista)
    return lista
for j in  range (0, len(lista)):
    if lista [j]%2==0:
        print("Pares:",lista[j], end=", ")

