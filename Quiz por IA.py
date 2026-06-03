x = int(input("Ingrese un Numero en Formato YYYYMMDD: "))

if 9999999 < x < 100000000:
    yyyy = x // 10000
    mm = (x % 10000) // 100
    dd = x % 100

    if 0 < mm < 13:
        # Definir días de cada mes
        e = 31  # enero
        f = 28  # febrero
        m = 31  # marzo
        a = 30  # abril
        ma = 31 # mayo
        ju = 30 # junio
        jul = 31 # julio
        ag = 31 # agosto
        se = 30 # septiembre
        o = 31  # octubre
        no = 30 # noviembre
        d = 31  # diciembre

        # Inicializar
        dias = dd
        mes_nombre = ""

        # Sumar los días anteriores y asignar nombre del mes
        if mm == 1:
            mes_nombre = "Enero"
        if mm == 2:
            dias += e
            mes_nombre = "Febrero"
        if mm == 3:
            dias += e + f
            mes_nombre = "Marzo"
        if mm == 4:
            dias += e + f + m
            mes_nombre = "Abril"
        if mm == 5:
            dias += e + f + m + a
            mes_nombre = "Mayo"
        if mm == 6:
            dias += e + f + m + a + ma
            mes_nombre = "Junio"
        if mm == 7:
            dias += e + f + m + a + ma + ju
            mes_nombre = "Julio"
        if mm == 8:
            dias += e + f + m + a + ma + ju + jul
            mes_nombre = "Agosto"
        if mm == 9:
            dias += e + f + m + a + ma + ju + jul + ag
            mes_nombre = "Septiembre"
        if mm == 10:
            dias += e + f + m + a + ma + ju + jul + ag + se
            mes_nombre = "Octubre"
        if mm == 11:
            dias += e + f + m + a + ma + ju + jul + ag + se + o
            mes_nombre = "Noviembre"
        if mm == 12:
            dias += e + f + m + a + ma + ju + jul + ag + se + o + no
            mes_nombre = "Diciembre"

        print(f"\nEl {dd} de {mes_nombre} del {yyyy} han transcurrido un total de {dias} días")

    else:
        print("Mes inválido")
else:
    print("Dato no valido. Debe ser YYYYMMDD")
