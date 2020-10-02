
Winner = False
Turn = False
NumTurn = 0
Place = ["","","","","","","","",""]
Pos = [1,2,3,4,5,6,7,8,9]
x = 1
y = 2

def beginning():
    print("Hola, sean bienvenidos a mi juego de TicTacToe.\nEl jugador numero 1 tendra el icono x.\nEl jugador numero 2 tendra el icono o.\nEl tablero esta ordenado por numeros del 1 al 9, tienes que escribir un numero entre ese rango\nSi la posicion que quieres seleccionar esta ocupada, por favor selecciona otra.\nBuena suerte y diviertete mucho :D")
    print("")
beginning()

def board():
    print(Place[0]+" I "+Place[1]+" I "+Place[2])
    print("------")
    print(Place[3]+" I "+Place[4]+" I "+Place[5])
    print("------")
    print(Place[6]+" I "+Place[7]+" I "+Place[8] + "\n ")


def player1(Ply):
    if Ply == Pos[Ply-1]:
        Pos[Ply-1] = "x"
        Place[Ply-1] = "x"
    else : 
        print("La posicion seleccionada no esta disponible.\nPor Favor Seleccione otra.")

def player2(Ply):
    if Ply == Pos[Ply-1]:
        Pos[Ply-1] = "o"
        Place[Ply-1] = "o"
    else : 
        print("La posicion seleccionada no esta disponible.\nPor Favor Seleccione otra.")

def Post(Ply):
    if Ply == Pos[Ply-1]:
        return 1
    else:
        return 0

def win():
 
    x1 = Pos[0] == Pos[1] == Pos[2] == "x"
    x2 = Pos[3] == Pos[4] == Pos[5] == "x"
    x3 = Pos[6] == Pos[7] == Pos[8] == "x"
    x4 = Pos[0] == Pos[4] == Pos[8] == "x"
    x5 = Pos[6] == Pos[4] == Pos[2] == "x"
    x6 = Pos[0] == Pos[3] == Pos[6] == "x"
    x7 = Pos[2] == Pos[5] == Pos[8] == "x"
    x8 = Pos[1] == Pos[4] == Pos[7] == "x"
    o1 = Pos[0] == Pos[1] == Pos[2] == "o"
    o2 = Pos[3] == Pos[4] == Pos[5] == "o"
    o3 = Pos[6] == Pos[7] == Pos[8] == "o"
    o4 = Pos[0] == Pos[4] == Pos[8] == "o"
    o5 = Pos[6] == Pos[4] == Pos[2] == "o"
    o6 = Pos[0] == Pos[3] == Pos[6] == "o"
    o7 = Pos[2] == Pos[5] == Pos[8] == "o"
    o8 = Pos[1] == Pos[4] == Pos[7] == "o"
    if x1 or x2 or x3 or x4 or x5 or x6 or x7 or x8:
        return x
    if o1 or o2 or o3 or o4 or o5 or o6 or o7 or o8:
        return y
    else:
        return 0

while Winner == False:
    board()
    if Turn == False:
        Ply = int(input("Turno del jugador 2: "))
        if Post(Ply) == 1:
            Turn = True
            NumTurn = NumTurn + 1
        player2(Ply)
    else:
        Ply = int(input("Turno del jugador 1: "))
        if Post(Ply) == 1:
            Turn = False
            NumTurn = NumTurn + 1
        player1(Ply)
    if Post(Ply) == 1:
        NumTurn = NumTurn + 1
    if NumTurn == 9 and Winner == False:
        board()
        print("Nadie ganó")
        exit()
    if win() == x:
        board()
        Winner = True
        print("El jugador 1 ha ganado")
    if win() == y:
        board()
        Winner = True
        print("El jugador 2 ha ganado")





