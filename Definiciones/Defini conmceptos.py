def hola():
    chao()
    print("hola")
def chao():
    print("chao")
hola()
print("fin")

def suma():
    a = 4
    b =7
    c = a + b
    print(c)
suma()

def multiplicacion():
    a = 3
    b = 5
    m = a * b
    return m
x = multiplicacion()
print(x)

def division(a,b):
    d = a / b
    print(d)
pedro = 7
steven = 2
division(pedro,steven)

def potencia (base, exponente):
    p = base ** exponente
    return p
p = potencia (2,3)
print(p)

def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    return f
def combinatoria(n,x):
    c=factorial(n)/(factorial(x)*factorial(n-x))
    return c
def inicio():
    n = int(input("digite n:"))
    x = int(input("digite n:"))
    c = combinatoria(n,x)
    print("la combinatoria de n=",n,"y x=",x,"es ",c )
inicio()
