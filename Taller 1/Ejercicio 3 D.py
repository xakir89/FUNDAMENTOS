# 3. Elaborar un algoritmo para cada uno de los siguientes problemas : 
#    a. Convertir de dólares a pesos 
#    b. Convertir de pesos a dólares 
#    c. Convertir de grados centígrados a Farenheit. 
#    d. Calcular el promedio de 3 números  

def ingreso(dato):
    x = float(input(f"""
.......................................
:         INGRESE NOTA {dato}             :
.......................................
"""))
    return x

def promedio(a,b,c):
    print("""
.......................................
:                                     :
:      PROMEDIO NOTAS, 3 MATERIAS     :
:                                     :
.......................................
""")
    pro = ( a + b + c ) / 3
    return pro

def tablero(pro,a,b,c):
    print(f"""
.......................................
:                                     :
:     PROMEDIO NOTAS, 3 MATERIAS      :
:                                     :
:           Nota 1: {a:.2f}              :
:           Nota 2: {b:.2f}              :
:           Nota 3: {c:.2f}              :
:                                     :
:         PROMEDIO: {pro:.2f}              :
:                                     :
.......................................
          """)
def main():
    a = ingreso("1 ")
    b = ingreso("2 ")
    c = ingreso("3 ")
    pro = promedio(a,b,c )
    tablero(pro,a,b,c)
main()

    
