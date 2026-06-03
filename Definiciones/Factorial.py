#definicion con factorial


def factorialfor(n):
    
    factorial = 1
    for i in range(1,n+1):
        anterior = factorial
        factorial *= i
        print(i,"X", anterior, "=" ,factorial)
    return factorial    
    
    
def factorialwhile(m):
    
    i = 1
    factorial=1
    while i <= m:
        anterior = factorial
        factorial *= i
        print(i,"X", anterior, "=" ,factorial)
        i += 1
    
    return(factorial)

def variables():
    n = int(input("Ingrese N:"))
    print()
    factor1 = factorialfor(n)
    print(f"\nfactorial con for {factor1}\n")
    m = int (input("ingrese m:"))
    print()
    factor2 = factorialwhile(m)
    print(f"\nfactorial con while {factor2}\n")
    return factor1, factor2
prueba= variables()
print=(prueba)
