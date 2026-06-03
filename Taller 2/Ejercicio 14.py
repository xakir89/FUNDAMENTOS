####################################################################################################
#   13. En una Universidad, los estudiantes tienen asignado un código de 8 cifras, en el que los 4 #
#   primeros dígitos indican el año de matrícula, y el que le sigue, el semestre del año (primero  #
#   o segundo); si se conoce el código de un estudiante, elabore un algoritmo que determine        #
#   en que año y en que semestre, ingreso a la Universidad.                                        #
####################################################################################################

codigo = int(input("ingrese Codigo Alumno: "))

while codigo < 10000000:
    print("codigo invalido el codigo solo tiene 8 digitos")
    codigo = int(input("ingrese Codigo Alumno: "))
while codigo > 99999999:
    print("codigo invalido el codigo solo tiene 8 digitos")
    codigo = int(input("ingrese Codigo Alumno: "))
    
semestre = (codigo%10000)//1000

while semestre < 1:
    print("codigo invalido despues del anio solo puede ser 1 o 2 referente al semestre")
    codigo = int(input("ingrese Codigo Alumno: "))
    semestre = (codigo%10000)//1000
while semestre > 2:
    print("codigo invalido despues del anio solo puede ser 1 o 2 referente al semestre")
    codigo = int(input("ingrese Codigo Alumno: "))
    semestre = (codigo%10000)//1000
anio = codigo//10000




print(f"\nEL CODIGO DEL ESTUDIANTE ES: {codigo}\nINGRESO EN EL ANIO:{anio}\nE INGRESO EN EL SEMESTRE: {semestre}")
