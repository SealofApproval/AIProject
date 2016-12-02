from Minesweeper import *
from random import randint


class AIMinesweeper:
   def __init__(self, game, size, numBombs):
      self.board = game
      self.defaultProb = numBombs/(size*size)
      self.probBoard = [["c" for x in range(0, size)] for y in range(0,size)]
      self.size = size
      self.numBombs = numBombs

   def getMove(self):
      minProb = 1.0
      moves = []
      for x in range(0, self.size):
         for y in range(0, self.size):
            if self.probBoard[x][y] == "c":
               value = self.defaultProb
            else:
               value = self.probBoard[x][y]
            if value == 1.0 and self.board[x][y] != "F":
               return ["f", x, y]
            elif value < minProb and self.board[x][y] == "X":
               minProb = value
               moves = [["m", x, y]]
            elif value == minProb and self.board[x][y] == "X":
               moves.append(["m", x, y])
      if len(moves) == 1:
         return moves[0]
      else:
         rand = randint(0, len(moves)-1)
         return moves[rand]

   def updateBoard(self, game):
      self.board = game
      self.probBoard = [["c" for x in range(0, self.size)] for y in range(0,self.size)]
      for x in range(0,self.size):
         for y in range(0, self.size):
            spaces = []
            if self.board[x][y] == "F":
               self.probBoard[x][y] = 1.0
            elif self.board[x][y] != "X":
               s = 0
               f = 0
               self.probBoard[x][y] = 0.0
               if self.board[x][y] == " ":
                  m = 0
               else:
                  m = self.board[x][y]
               for a in range(max(x-1, 0), min(x+2, self.size)):
                  for b in range(max(y-1,0), min(y+2, self.size)):
                     if self.board[a][b] == "F":
                        f = f + 1
               if m-f == 0:
                  for a in range(max(x-1, 0), min(x+2, self.size)):
                     for b in range(max(y-1,0), min(y+2, self.size)):
                        if self.board[a][b] == "X":
                           self.probBoard[a][b] = 0.0
               else:
                  f = 0
                  for a in range(max(x-1, 0), min(x+2, self.size)):
                     for b in range(max(y-1,0), min(y+2, self.size)):
                        if self.board[a][b] == "X" and self.probBoard[a][b] != 0.0:
                           spaces.append([a,b])
                           s = s + 1
                        if self.board[a][b] == "F":
                           f = f + 1
                  if s != 0:
                     prob = (m-f)/s
                     for a in spaces:
                        value = 0
                        f = a[0]
                        g = a[1]
                        if self.probBoard[f][g] == "c":
                           value = self.defaultProb
                        else:
                           value = self.probBoard[f][g]
                        if prob > value:
                           self.probBoard[f][g] = prob

      f = 0
      z = 0
      for x in range(0, self.size):
         for y in range(0, self.size):
            if self.board[x][y] == "F":
               f = f + 1
            if self.board[x][y] == "X":
               z = z + 1
      self.defaultProb = (self.numBombs - f)/ z
