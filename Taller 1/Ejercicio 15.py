print("\n Area Franja Amarilla de una Circunferencia y un Trapesio \n")
A = float(input("Ingresa valor de A:"))#DIAMETRO DE LA CIRCUNFERENCIA Y BASE MAYOR DEL TRAPESIO
B = float(input("Ingresa valor de B:"))#ALTURA DEL TRAPESIO
C = float(input("Ingresa valor de C:"))#BASE MENOR DEL TRAPESIO

r = A/2 # r es radio por eso lo divido por dos
AC = 3.1416*(r**2)
ATR = ((A+C)*B)/2
AFA = AC-ATR

print(f"\n AREA FRANJA AMARILLA SIENDO EL AREA DE LA CIRCUNFERENCIA:{AC} MENOS EL AREA DEL TRAPESIO:{ATR}\n EL RESULTADO ES :{AFA}")
