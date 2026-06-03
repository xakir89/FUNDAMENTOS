# --- Tus funciones originales con ajustes mínimos ---

def capturarn():
    n = int(input("Ingrese cantidad de numeros que van a entrar a la lista:"))
    return n

def cacturarnumeros(n):
    lista = []
    for i in range(0, n):
        x = int(input("digite un numero: "))
        lista.append(x)
    return lista  # CAMBIO: Antes devolvías 'x', ahora devuelves la 'lista' completa

def promedioPar(lista): # CAMBIO: Agregamos (lista) para que la función pueda ver los datos
    acu = 0
    con = 0
    for i in range(0, len(lista)):
        if lista[i] % 2 == 0:
            acu = acu + lista[i]
            con = con + 1
    
    # CAMBIO: El cálculo y el print van FUERA del for para que no se repitan
    if con > 0:
        pro = acu / con
        print("Promedio de los pares:", pro) # CAMBIO: 'pro' en lugar de 'prom'
    else:
        print("No hay pares en la lista")

def promedioimpar(lista): # CAMBIO: Agregamos (lista)
    acu = 0
    con = 0
    for i in range(0, len(lista)):
        if lista[i] % 2 == 1:
            acu = acu + lista[i]
            con = con + 1
            
    # CAMBIO: El cálculo y el print van FUERA del for
    if con > 0:
        pro = acu / con
        print("Promedio de los Impares:", pro) # CAMBIO: 'pro' en lugar de 'prom'
    else:
        print("No hay impares en la lista")

def inicio():
    n = capturarn()
    lista_datos = cacturarnumeros(n) # Guardamos la lista que devuelve la función
    promedioPar(lista_datos) # Se la enviamos a la función de pares
    promedioimpar(lista_datos) # Se la enviamos a la función de impares

# --- Ejecución ---
inicio()
