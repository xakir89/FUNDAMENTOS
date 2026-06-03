x = int(input("ingrese un numero de cuatro digitos:"))
if 999 < x < 10000:
    ab = x//100
    cd = x%100
    if ab > cd:
        a = x//1000
        b = (x%1000)//100
        c = (x%100)//10
        d = x%10
        ST = a+b+c+d
        print(f"Suma de a + b + c + d es igual a {ST}")
        
    else:
        ST = ab + cd
        print(f"Suma de ab {ab} mas cd {cd} es igual a {ST}")
else:
    print("Error dato no valido el ingreso debe tener 4 digitos")
