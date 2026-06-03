def rango(pos):
    r = False
    if pos>=1 and pos<=9:
        r = True
    return r
def asignar(t,pos,s):
    t[pos]=s
    return t
def hayjuego(t):
    hj = False
    for i in range(1,10):
        if t[i]==i:
            hj = True
    return hj
def poslibre(t,pos):
    pl = False
    if t[pos]==pos:
        pl = True
    return pl 
def ganador(t,s):
    g = False
    if((t[1]==s and t[2]==s and t[3]==s) or
       (t[4]==s and t[5]==s and t[6]==s) or
       (t[7]==s and t[8]==s and t[9]==s) or
       (t[1]==s and t[4]==s and t[7]==s) or
       (t[2]==s and t[5]==s and t[8]==s) or
       (t[3]==s and t[6]==s and t[9]==s) or
       (t[1]==s and t[5]==s and t[9]==s) or
       (t[3]==s and t[5]==s and t[7]==s)):
        g = True
    return g
def mostrar(t):
    print(t[1],"|",t[2],"|",t[3])
    print("---------")
    print(t[4],"|",t[5],"|",t[6])
    print("---------")
    print(t[7],"|",t[8],"|",t[9])
    
def inicio():
    t =[0,1,2,3,4,5,6,7,8,9]
    
    
    j = False

    while j==False:
        mostrar(t)
        r = False
        while r == False:
            pos = int(input("digite la pos J1:"))
            r = rango(pos)
            if rango(pos):
                if hayjuego(t):
                    pl = False
                    while pl==False:
                        pl=poslibre(t,pos)
                        if pl:
                            t = asignar(t,pos,"x")
                            if ganador(t,"x"):
                                print("Jugador 1 Ganó, x")
                                j = True
                            else:
                                if hayjuego(t)==False:
                                    print("fin del juego")
                                    j = True
                        else:
                            pos = int(input("digite la pos J1:"))
                else:
                    print("fin del juego")
                    j = True
                    
        if j == False:
            mostrar(t)
            r = False
            while r == False:
                pos = int(input("digite la pos J2:"))
                r = rango(pos)
                if rango(pos):
                    if hayjuego(t):
                        pl = False
                        while pl==False:
                            pl=poslibre(t,pos)
                            if pl:
                                t = asignar(t,pos,"o")
                                if ganador(t,"o"):
                                    print("Jugador 2 Ganó, o")
                                    j = True
                                else:
                                    if hayjuego(t)==False:
                                        print("fin del juego")
                                        j = True
                            else:
                                pos = int(input("digite la pos J2:"))
                    else:
                        print("fin del juego")
                        j = True
     
    
    
    

inicio()
