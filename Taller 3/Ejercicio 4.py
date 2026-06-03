print(f"4. Diseñe un algoritmo que imprima las siguientes series para (n) terminos:\n ● 1, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44 . . .")
n = int(input(f"Ingrese el valor de n:\n"))
for i in range(1, n+1):
    if i == 1:
        print(1, end=",")
    else:
        print((i-1)*4, end=",")
print("...")

print(f"● 1, 4, 9, 16, 25, 36, 49, 64, 81 . . .")
for i in range (1,n+1):
    print(i*i, end=",")
print("...")

print(f"● 2, 4, 6, 8, 10, 12 . . .")
for i in range (1,n+1):
    print(i*2,end=",")
print("...")

print(f"● -2, +4, -6, +10, -16, +26,. . .")
a, b = 2, 4

for i in range(1, n + 1):
    # Imprimimos el valor actual con su signo
    signo = "+" if i % 2 == 0 else "-"
    print(f"{signo}{a}", end=",")
    
    # Avanzamos la serie: el nuevo 'a' es el viejo 'b', 
    # y el nuevo 'b' es la suma de ambos.
    a, b = b, a + b

print("...")



for i in range(1, n + 1):
    # LÓGICA MATEMÁTICA:
    # 1. El signo se define por (-1) elevado a la potencia i
    # 2. Multiplicamos ese 1 o -1 por el valor de 'a'
    valor_con_signo = ((-1)**i) * a
    
    # Formateamos para que muestre el "+" si es positivo
    print(f"{valor_con_signo:+d}", end=", ")
    
    # Actualización de Fibonacci
    a, b = b, a + b

print("...")




for i in range(1, n + 1):
    # 1. Lógica Matemática: Determinamos el signo con un IF
    if i % 2 != 0:
        actual = a * -1  # Si la vuelta es impar, multiplicamos por -1
    else:
        actual = a * 1   # Si es par, se queda positivo (multiplicar por 1)
    
    # 2. Impresión con formato
    print(f"{actual:+d}", end=", ")
    
    # 3. Evolución de la serie (Suma recurrente)
    a, b = b, a + b

print("...")
