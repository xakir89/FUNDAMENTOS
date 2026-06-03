print("\n AREA TRIANGULO, AREA ROMBO, AREA TRAPESIO \n")
bt = float(input("Ingresa Base del Triangulo:"))
ht = float(input("Ingresa Altura del Triangulo:"))
AT = (bt*ht)/2

Dr = float(input("Ingresa Diagonal mayor del Rombo:"))
dr = float(input("Ingresa Diagonal menor del Rombo:"))
AR = (Dr*dr)/2

Btr = float(input("Ingresa Base mayor del Trapesio:"))
btr = float(input("Ingresa Base menor del Trapesio:"))
htr = float(input("Ingresa Altura del Trapesio:"))
ATR = ((Btr+btr)*htr)/2

print(f"\n Area del Triangulo es base {bt} por altura {ht} divido 2 = {AT} \n")
print(f"\n Area del Rombo  es Diagonal mayor {Dr} por diagonal menor {dr} divido 2 = {AR} \n")
print(f"\n Area del Trapesio es Base mayor {Btr} por base menor {btr} por Altura del trapesio {htr} divido 2 = {ATR} \n")
