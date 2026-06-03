
#9. Elaborar un algoritmo que convierta una medición de tiempo en segundos a: horas,minutos y segundos. Ejemplo: Sea 34505
#la cantidad digitada en segundos, se debe mostrar por pantalla Horas = 9, Minutos = 35, Segundos = 5.

X = int(input("Ingrese la cantidad de segundos a cambiar:"))

Horas = X//3600
Minutos = (X%3600)//60
Segundos = (X%3600)%60

print(f"HORAS:{Horas} MINUTOS:{Minutos} SEGUNDOS:{Segundos}")


