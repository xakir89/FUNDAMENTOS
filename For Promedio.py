n = int(input("Ingrese un numero:"))
acu = 0
con = 0
for i in range(1,n+1):
    x = int(input(f"\nIngrese un numero:"))
    if x%2==0:
        acu = acu + x
        con = con + 1
if con > 0:
    pro = acu/ con
    print(f"\nel preomedio de los pares es {pro}")
else:
    print(f"\nno hay numeros pares")
    
                                                                                                              
