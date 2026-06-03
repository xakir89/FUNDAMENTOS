a = float(input("Digite su Numero para a:"))
b = float(input("Digite su Numero para b:"))
c = float(input("Digite su Numero para c:"))

p = (a+b+c)/2
P = (p*(p-a)*(p-b)*(p-c))**0.5
 
print()
print("RESULTADO DEL SEMIPERIMETRO")
print()
print("Semiperimetro del triangulo:", p)
print()
print("RESULTADO DEL AREA:")
print()
print("AREA:", P)
