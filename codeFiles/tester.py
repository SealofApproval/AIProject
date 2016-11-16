from Minesweeper import *
from AIMinesweeper import *

play = True
cont = True
win = False

while play:
   size = int(input("Please enter the size of the board: "))
   numBombs = int(input("Please enter the number of bombs: "))
   game = Minesweeper(numBombs, size)
   game.printBoard()
   player = AIMinesweeper(game.returnBoard(), size, numBombs)
   while cont:
      move = player.getMove()
      if move[0] == "m":
         cont = game.processMove(move[1], move[2])
         game.printBoard()
         win = game.checkWin()
         if win or not cont:
            cont = False
         else:
            player.updateBoard(game.returnBoard())
      elif move[0] == "f":
         result = game.processFlag(move[1], move[2])
         game.printBoard()
         win = game.checkWin()
         if win:
            cont = False
         else:
            player.updateBoard(game.returnBoard())
   if win:
      print("Congrats! You won the Game!")
   else:
      player.printProbBoard()
      print("Oh No! You encountered a bomb!")
   choice = input("Would you like to play again? (y or n): ")
   if choice == "n":
      play = False
   else:
      cont = True

input('Press Enter to exit')
