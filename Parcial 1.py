n = int(input(""))

cont = 1
signo = ""

# Fibonacci impar
a = 0
b = 0
c = 1

# Secuencia par
A = 2
B = 2
C = 4

d = 1

for i in range(1, n + 1):

    # patrón de signos
    if cont <= 2:
        signo = "-"
    else:
        signo = "+"

    # IMPARES -> 0 1 1 2 3 5
    if i % 2 != 0:

        if i == 1:
            num = 0

        if i == 3:
            num = 1

        if i > 3:
            a = b
            b = c
            c = a + b
            num = c

        # factorial impar
        F = 1

        for j in range(1, num + 1):
            F *= j

        print(signo, F, end=" ")

    # PARES -> 2 4 6 10 16 26
    if i % 2 == 0:

        if i == 2:
            num2 = 2

        if i == 4:
            num2 = 4

        if i > 4:
            A = B
            B = C
            C = A + B
            num2 = C

        # factorial par
        F = 1

        for j in range(1, num2 + 1):
            F *= j

        print(signo, F, "/", d, end=" ")

        d += 1

    cont += 1

    if cont == 6:
        cont = 1
