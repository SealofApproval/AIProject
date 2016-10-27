from Minesweeper import *

play = True
cont = True
win = False
game = Minesweeper(5, 10)
game.printBoard()

while play:
    while cont:
        move = input("Please enter f to add or remove a flag, or m to enter cordinates to move: ")
        result = -1
        if move == "m":
            x = int(input('Please enter a x value: '))
            y = int(input('Please enter a y value: '))
            cont = game.processMove(x, y)
            game.printBoard()
            win = game.checkWin()
            if win:
                cont = False
        elif move == "f":
            while result != 0:
                x = int(input('Please enter a x value: '))
                y = int(input('Please enter a y value: '))
                result = game.processFlag(x, y)
                if result == 0:
                    game.printBoard()
                elif result == 1:
                    print("That location has a known value. Please enter a new location.")
                else:
                    print("That is an invalid location. Please enter a new location.")
            game.printBoard()
            win = game.checkWin()
            if win:
                cont = False
        else:
            print("That is not a valid command decision. Please try again.")
    if win:
        print("Congrats! You won the Game!")
    else:
        print("Oh No! You encountered a bomb!")
    choice = input("Would you like to play again? (y or n): ")
    if choice == "n":
        play = False
    else:
        cont = True

input('Press Enter to exit')
