# 8. Diseñe un algoritmo que permita calcular los N primeros te
#́rminos de la serie Fibonacci (N es ingresada por el usuario).
n = int(input("ingrese valor de n:"))
con = 1
simbolo = ""
for i in range (1,n+1):
    if con < 3:
        simbolo = "-"
    else:
        simbolo = "+"
    print(simbolo)
    con = con + 1
    if con ==6:
        con = 1
        
    
    
