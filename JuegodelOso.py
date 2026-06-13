def rango(pos):
    r = False
    if pos >=0 and pos <=16:
        r = True
    return r
def assignarpos(o,pos,simbolo):
    o[pos] = simbolo
    return simbolo
def poslibre(o,pos):
    pl = False
    if o[pos] == pos:
        pl = True
    return pl
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