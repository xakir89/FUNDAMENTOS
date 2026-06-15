def rango(pos):
    r = False
    if pos >=0 and pos <=16:
        r = True
    return r
def asignarpos(o,pos,simbolo):
    o[pos] = simbolo
    return simbolo
def hayjuegoo(o):
    hj = False
    for i in range(16):
        if o[i] == i:
            hj = True
    return hj
def poslibre(o,pos):
    pl = False
    if o[pos] == pos:
        pl = True
    return pl
def ganador(o,simbiolo):
    g = False
    if((o[0]==simbiolo and o[1]==simbiolo and o[2]==simbiolo and o[3]==simbiolo) or
       (o[4]==simbiolo and o[5]==simbiolo and o[6]==simbiolo and o[7]==simbiolo) or
       (o[8]==simbiolo and o[9]==simbiolo and o[10]==simbiolo and o[11]==simbiolo) or
       (o[12]==simbiolo and o[13]==simbiolo and o[14]==simbiolo and o[15]==simbiolo) or
       (o[0]==simbiolo and o[4]==simbiolo and o[8]==simbiolo and o[12]==simbiolo) or
       (o[1]==simbiolo and o[5]==simbiolo and o[9]==simbiolo and o[13]==simbiolo) or
       (o[2]==simbiolo and o[6]==simbiolo and o[10]==simbiolo and o[14]==simbiolo) or
       (o[3]==simbiolo and o[7]==simbiolo and o[11]==simbiolo and o[15]==simbiolo)):
        g = True
def mostrar(O):
    o= O
    print("\n.............................\n¡Bienvenido al juego del oso!\n.............................\n")
    print("| ",o[0],"|", o[1]," |", o[2]," |", o[3]," |")
    print("| ",o[4],"|", o[5]," |", o[6]," |", o[7]," |")
    print("| ",o[8],"|", o[9],"|", o[10],"|", o[11],"|")
    print("|",o[12],"|", o[13],"|", o[14],"|", o[15],"|\n")

def jugar():
    
    o = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    mostrar(o)
jugar()