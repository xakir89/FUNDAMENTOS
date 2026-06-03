print("\n Area Franja Amarilla de una Circunferencia y un Trapesio \n")
A = float(input("Ingresa valor de A:"))#Base menor Trapesio
B = float(input("Ingresa valor de B:"))# l
C = float(input("Ingresa valor de C:"))#BASE MENOR DEL TRAPESIO
D = float(input("Ingresa valor de D:"))#BASE MENOR DEL TRAPESIO

atr = D-B # Altura del trapesio
AT = (C*B)/2# Area Triangulo
ATR = ((C+A)*atr)/2 # area Trapesio
SAF = AC-ATR # Suma Area Total

print(f"\n AREA FRANJA AMARILLA SIENDO EL AREA DE LA CIRCUNFERENCIA:{AC} MENOS EL AREA DEL TRAPESIO:{ATR}\n EL RESULTADO ES :{AFA}")
