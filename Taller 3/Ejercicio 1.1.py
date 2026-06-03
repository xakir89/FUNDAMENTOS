x = int(input("Ingrese el numero base (x):"))
n = int(input("Cuantos multiplos quieres (n):"))
valido = n > 0
if valido:
    acu_suma = 0
    print(f"\nlos Primeros Multiplos {n} de {x} son:\n")
    for i in range (1,n+1):
        multiplo = x*i
        print(f"Multiplo de i {i} por base {x} = {multiplo}")
        acu_suma = acu_suma + multiplo
    print(f"\nla suma La suma total del conjunto {acu_suma}")
else:
    print(f"no puede ser menor de cero")
