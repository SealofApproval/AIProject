from Minesweeper import *
from AIMinesweeper import *

play = True
cont = True
win = False
sizes = [20, 20, 20, 10, 20, 20, 20, 10, 10, 5, 5, 10, 10, 10, 10, 10]
bombs = [5, 10, 15, 5, 20, 25, 30, 10, 15, 4, 5, 20, 25, 30, 35, 40]
counter = 0
trials = 0
wins = 0
fails = 0

while counter < len(sizes):
   game = Minesweeper(bombs[counter], sizes[counter])
   game.printBoard()
   player = AIMinesweeper(game.returnBoard(), sizes[counter], bombs[counter])
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
      wins = wins + 1
   else:
      print("Oh No! You encountered a bomb!")
      fails = fails + 1
   cont = True
   trials = trials + 1
   if trials == 100:
      print("Wins: " + str(wins))
      print("Losses: " + str(fails))
      trials = 0
      wins = 0
      fails = 0
      counter = counter + 1
      waste = input("Hit enter to continue")
   
   
   
input('Press Enter to exit')
