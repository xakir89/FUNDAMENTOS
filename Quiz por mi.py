x = int(input("Ingrese un Numero en Formato YYYYMMDD"))
if 9999999 < x < 100000000:
    yyyy = x // 10000
    mm = (x % 10000) // 100
    dd = x % 100
    if 0 < mm < 13:
        e = 31
        f = 28
        m = 31
        a = 30
        ma = 31
        ju = 30
        jul = 31
        ag = 31
        se = 30
        o = 31
        no = 30
        if mm == 1:
            print(f"\nel {dd} de Enero del {yyyy} han trascurrido un total de {dd} dias")
        if mm == 2:
            f1 = e + dd
            print(f"\nel {dd} de Febrero del {yyyy} han trascurrido un total de {f1} dias")
        if mm == 3:
            m1 = e + f + dd
            print(f"\nel {dd} de Marzo del {yyyy} han trascurrido un total de {m1} dias")
        if mm == 4:
            a1= e + f + m + dd
            print(f"\nel {dd} de Abril del {yyyy} han trascurrido un total de {a1} dias")
        if mm == 5:
            ma1 = e + f + m + a + dd
            print(f"\nel {dd} de Mayo del {yyyy} han trascurrido un total de {ma1} dias")
        if mm == 6:
            ju1 = e + f + m + a + ma + dd
            print(f"\nel {dd} de Junio del {yyyy} han trascurrido un total de {ju1} dias")
        if mm == 7:
            jul1 = e + f + m + a + ma + ju + dd
            print(f"\nel {dd} de Julio del {yyyy} han trascurrido un total de {jul1} dias")
        if mm == 8:
            ag1 = e + f + m + a + ma + ju + jul + dd
            print(f"\nel {dd} de Agosto del {yyyy} han trascurrido un total de {ag1} dias")
        if mm == 9:
            se1 =  e + f + m + a + ma + ju + jul + ag + dd
            print(f"\nel {dd} de Septiembre del {yyyy} han trascurrido un total de {se1} dias")
        if mm == 10:
            o1 =  e + f + m + a + ma + ju + jul + ag + se + dd
            print(f"\nel {dd} de Octubre del {yyyy} han trascurrido un total de {o1} dias")
        if mm == 11:
            no1 =  e + f + m + a + ma + ju + jul + ag + se + o + dd
            print(f"\nel {dd} de Noviembre del {yyyy} han trascurrido un total de {no1} dias")
        if mm == 12:
            d =  e + f + m + a + ma + ju + jul + ag + se + o + no + dd
            print(f"\nel {dd} de Diciembre del {yyyy} han trascurrido un total de {d} dias")
else:
    print(f"Dato no valido Fecha en YYYYMMDD")
