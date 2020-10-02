def revisarSudoku(sudoku):
    for row in sudoku:
        if not (1 in row and 2 in row and 3 in row and 4 in row and 5 in row and 6 in row and 7 in row and 8 in row and 9 in row):
            return False
    for x in range(9):
        col = [item[x] for item in sudoku]
        if not (1 in col and 2 in col and 3 in col and 4 in col and 5 in col and 6 in col and 7 in col and 8 in col and 9 in col):
            return False
    for y in range(0, 9, 3):
        box = []
        for z in range(0, 9, 3):
            box.append(sudoku[y][z:z+3] + sudoku[y+1][z:z+3] + sudoku[y+2][z:z+3])
        if not (1 in box[0] and 2 in box[0] and 3 in box[0] and 4 in box[0] and 5 in box[0] and 6 in box[0] and 7 in box[0] and 8 in box[0] and 9 in box[0]):
            return False
    return True 






    # for j in range(3):
    #     for z in range(3):
    #         for w in range(3):
    #             for y in range(3):
    #               sudoku[y+3*z][x+3*j]
                        


        # Primero considerar los primeros 3 numeros
        # saltarme la row abajo 2 veces mas
        # varios "for" sumando de tres en tres

    



sudoku = []
linea1 = input("Escribe tu primer fila de numeros separados por un espacio: ")
linea2 = input("Escribe tu segunda fila de numeros separados por un espacio: ")
linea3 = input("Escribe tu tercer fila de numeros separados por un espacio: ")
linea4 = input("Escribe tu cuarta fila de numeros separados por un espacio: ")
linea5 = input("Escribe tu quinta fila de numeros separados por un espacio: ")
linea6 = input("Escribe tu sexta fila de numeros separados por un espacio: ")
linea7 = input("Escribe tu septima fila de numeros separados por un espacio: ")
linea8 = input("Escribe tu octava fila de numeros separados por un espacio: ")
linea9 = input("Escribe tu novena fila de numeros separados por un espacio: ")
Slinea1= linea1.split(" ")
Slinea2= linea2.split(" ")
Slinea3= linea3.split(" ")
Slinea4= linea4.split(" ")
Slinea5= linea5.split(" ")
Slinea6= linea6.split(" ")
Slinea7= linea7.split(" ")
Slinea8= linea8.split(" ")
Slinea9= linea9.split(" ")

ISlinea1 = [int(x) for x in Slinea1]
ISlinea2 = [int(x) for x in Slinea2]
ISlinea3 = [int(x) for x in Slinea3]
ISlinea4 = [int(x) for x in Slinea4]
ISlinea5 = [int(x) for x in Slinea5]
ISlinea6 = [int(x) for x in Slinea6]
ISlinea7 = [int(x) for x in Slinea7]
ISlinea8 = [int(x) for x in Slinea8]
ISlinea9 = [int(x) for x in Slinea9]


sudoku.append(ISlinea1)
sudoku.append(ISlinea2)
sudoku.append(ISlinea3)
sudoku.append(ISlinea4)
sudoku.append(ISlinea5)
sudoku.append(ISlinea6)
sudoku.append(ISlinea7)
sudoku.append(ISlinea8)
sudoku.append(ISlinea9)


print(ISlinea1)
print(ISlinea2)
print(ISlinea3)
print(ISlinea4)
print(ISlinea5)
print(ISlinea6)
print(ISlinea7)
print(ISlinea8)
print(ISlinea9)

print(revisarSudoku(sudoku))


# sudokuCorrecto = [[8,2,7,1,5,4,3,9,6],
#                   [9,6,5,3,2,7,1,4,8],
#                   [3,4,1,6,8,9,7,5,2],
#                   [5,9,3,4,6,8,2,7,1],
#                   [4,7,2,5,1,3,6,8,9],
#                   [6,1,8,9,7,2,4,3,5],
#                   [7,8,6,2,3,5,9,1,4],
#                   [1,5,4,7,9,6,8,2,3],
#                   [2,3,9,8,4,1,5,6,7]]

