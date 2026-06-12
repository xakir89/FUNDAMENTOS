matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("----------MATRIX----------")
print("      ANDERSON LOPEZ      ")
print("--------------------------")
for fila in matrix:

    for columna in fila:
        print(" | ",columna," | ",end="")
    
    print("")
    print("--------------------------")

rows = int(input("cuantas Filas desea?: "))
Columns = int(input("Cuantas Columnas desea?: "))
matrices = []
for row_position in range(rows):
    row = []
    for column_position in range(Columns):
        row.append(int(input(f"ingrese un elemento para la Fila {row_position} :" )))
    matrices.append(row)
print("----------MATRIX----------")
print("      ANDERSON LOPEZ      ")
print("--------------------------")
for row in matrices:
    for column in row:
        print(" | ",column," | ",end="")
    print("")
    print("--------------------------")