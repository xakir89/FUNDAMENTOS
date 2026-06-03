###############################################################################################
#   12. Elaborar un algoritmo que lea un número de tres (3) cifras e indique si el dígito que #
#   representa las centenas es par.                                                           #
###############################################################################################

x = int(input("Número de 3 digitos: "))

while x<100:
    x = int(input("Número de 3 digitos: "))
while x>1000:
    x = int(input("Número de 3 digitos: "))

u = (x%100)%10
d = (x%100)//10
c= x//100

if c%2==0:
    print(f"\nla Centena es par {c} \n")
else:
    print(f"\nla Centena es impar {c} \n")
    
print(f"unidad = {u} decena = {d} centena= {c}")

