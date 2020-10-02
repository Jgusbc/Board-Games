import random
import time
nums = {}
print("Welcome to the Memory Game!!")


def memoryGame():
    lengthB = int(input("Specify the lenght of your board: "))
    widhtB = int(input("Specify the width of your board: "))
    extra = (lengthB*widhtB)%2    
    while extra != 0:
        print("The board you made is wrong.\nPlease create a board with a multiplication that results in an even number.")
        lengthB = int(input("Specify the lenght of your board: "))
        widhtB = int(input("Specify the width of your board: "))
        extra = (lengthB*widhtB)%2
        if extra == 0:
            break   
    even = (lengthB*widhtB)/2
    win = False
    board = []
    board_answer = []

    print("Excelent!")
    time.sleep(0.5)
    print("Creating Board.")
    time.sleep(1)
    print("Creating Board..")
    time.sleep(1)
    print("Creating Board...")
    time.sleep(3)
    print("Let's Play!")
    for i in range(0,lengthB):
        lista = []
        for j in range(0,widhtB):
            lista.append("Ω")
        board.append(lista)
    for x in board:
        print(x)

    for i in range(0,lengthB):
        lista = []
        for j in range(0,widhtB):
            randomNumber(lista,even)
        board_answer.append(lista)
      
    while win == False:
        row1 = int(input("Write the row of your first card:"))
        while row1 > lengthB :
            print("That row is out of range, please select another one!")
            row1 = int(input("Write the row of your first card:"))
            if row1 <= lengthB:
                break
        col1 = int(input("Write the column of your first card:"))
        while col1 > widhtB:
            print("That column is out of range, please select another one")
            col1 = int(input("Write the column of your first card:"))
            if col1 <= widhtB:
                break
        row2 = int(input("Write the row of your second card:"))
        while row2 > lengthB:
            print("That row is out of range, please select another one!")
            row2 = int(input("Write the row of your second card:"))
            if row2 <= lengthB:
                break
        col2 = int(input("Write the column of your second card:"))
        while col2 > widhtB:
            print("That column is out of range, please select another one")
            col2 = int(input("Write the column of your second card:"))
            if col2<= widhtB:
                break
        if board[row1-1][col1-1] != "Ω" or board[row2-1][col2-1] != "Ω":
            print("you already found that pair")
            for x in board:
                print(x)

        
        if board_answer[row1-1][col1-1] == board_answer[row2-1][col2-1]:
            board[row1-1].pop(col1-1)
            board[row1-1].insert(col1-1,board_answer[row1-1][col1-1])
            board[row2-1].pop(col2-1)
            board[row2-1].insert(col2-1,board_answer[row2-1][col2-1])
            for x in board:
                print(x)
            print("You have found a pair")
        else:
            board[row1-1].pop(col1-1)
            board[row1-1].insert(col1-1,board_answer[row1-1][col1-1])
            board[row2-1].pop(col2-1)
            board[row2-1].insert(col2-1,board_answer[row2-1][col2-1])
            for x in board:
                print(x)
            print("oh oh, try again")
            board[row1-1].pop(col1-1)
            board[row1-1].insert(col1-1,"Ω")
            board[row2-1].pop(col2-1)
            board[row2-1].insert(col2-1, "Ω")
            for x in board:
                print(x)
        if board == board_answer:
            win = True
    for x in board:
        print(x)
    print("Congratulations! You have won the game!")
    answer = input("Do you want to play again?: ")
    if answer == "yes" or answer == "Yes":
        win = False
        nums.clear()
        board.clear()
        board_answer.clear()
        memoryGame()
    elif answer == "no" or answer == "no":
        print("Thanks For Playing!")
        exit()
    
def randomNumber(lista,even):
    
    numR = random.randint(1,even)
    if numR in nums and nums[numR] == 2:
        randomNumber(lista,even)
    elif numR not in nums:
        nums[numR] = 1
        lista.append(numR)
    elif numR in nums and nums[numR] == 1:
        nums[numR] += 1
        lista.append(numR)
memoryGame()
    
