# 8. Diseñe un algoritmo que permita calcular los N primeros te
#́rminos de la serie Fibonacci (N es ingresada por el usuario).
n = int(input("ingrese valor de n:"))
a=0
b=1
c=0
for i in range(1,n+1):
    print(c)
    a=b
    b=c
    c=a+b
    
