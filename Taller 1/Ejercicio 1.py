A = float(input("Digite su Numero para A:"))
if (A-5)**2 > 0:
    a = float(input("Digite su Numero para a:"))
    b = float(input("Digite su Numero para b:"))
    c = float(input("Digite su Numero para c:"))
    X = float(input("Digite su Numero para X:"))
    EJ1 = (100-200)/(A-5)
    EJ2 = 15-((A**2)/3)
    EJ3 = a**2+b**2-35*c
    EJ4 = 5*X**2-3*X+5
    EJ5 = a**0.5+ b**0.5
    EJ6 = a**10-5
    print(f"\n RESULTADO DE LAS ECUACIONES \n\n Ejercicio a: {EJ1} \n Ejercicio b: {EJ2} \n Ejercicio c: {EJ3} Ejercicio d: {EJ4} \n Ejercicio e: {EJ5}\n Ejercicio f: {EJ6}")

else:
    print(f"A debe ser diferente de 5")

