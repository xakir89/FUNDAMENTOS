# 8. Diseñe un algoritmo que permita calcular los N primeros te
#́rminos de la serie Fibonacci (N es ingresada por el usuario).
n = int(input("ingrese valor de n:"))
num = 1
den = 2
simbolo = ""
for i in range(1,n+1):
    f = 1
    for j in range(1,den+1):
        f = f * j
    if i % 2 == 0:
        simbolo = "-"
    else:
        simbolo = "+"
    print(simbolo, num, "/",f)

    num = num + 2
    den = den + 2
    
