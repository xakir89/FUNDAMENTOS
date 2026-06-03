n= int(input("digite n: "))
periodo=""

for i in range (1,n+1):
    numerador=i*2-1
    denominador=i*2
    potencia=denominador
    if (i-1)%8<4:
        periodo="+"
    else:
        periodo="-"
        
    if numerador==1:
        print(periodo,numerador,"/",denominador, end=" ")
    else:
        print(periodo,numerador,"^",potencia,"/",denominador,end=" ")

