####################################################################################################
#                                                                                                  #    
#    3. Elabore un algoritmo que descomponga un número entero de tres cifras en sus dígitos y      #
#                luego imprima cada uno de ellos en letras (123 = uno dos tres).                   #
#                                                                                                  #
####################################################################################################

Numero = int(input("Ingrese Un NUMERO de 3 Digitos:"))
if 99 < Numero < 1000:
    centena = Numero // 100
    decena = (Numero % 100)//10
    unidad = Numero % 10
    print("El número en letras es:", end=" ")
    
    if centena == 0: print("CERO", end=" ")
    if centena == 1: print("UNO", end=" ")
    if centena == 2: print("DOS", end=" ")
    if centena == 3: print("TRES", end=" ")
    if centena == 4: print("CUATRO", end=" ")
    if centena == 5: print("CINCO", end=" ")
    if centena == 6: print("SEIS", end=" ")
    if centena == 7: print("SIETE", end=" ")
    if centena == 8: print("OCHO", end=" ")
    if centena == 9: print("NUEVE", end=" ")

    if decena == 0: print("CERO", end=" ")
    if decena == 1: print("UNO", end=" ")
    if decena == 2: print("DOS", end=" ")
    if decena == 3: print("TRES", end=" ")
    if decena == 4: print("CUATRO", end=" ")
    if decena == 5: print("CINCO", end=" ")
    if decena == 6: print("SEIS", end=" ")
    if decena == 7: print("SIETE", end=" ")
    if decena == 8: print("OCHO", end=" ")
    if decena == 9: print("NUEVE", end=" ")

    if unidad == 0: print("CERO")
    if unidad == 1: print("UNO")
    if unidad == 2: print("DOS")
    if unidad == 3: print("TRES")
    if unidad == 4: print("CUATRO")
    if unidad == 5: print("CINCO")
    if unidad == 6: print("SEIS")
    if unidad == 7: print("SIETE")
    if unidad == 8: print("OCHO")
    if unidad == 9: print("NUEVE")
