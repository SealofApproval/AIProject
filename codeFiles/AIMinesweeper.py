## File AIMinesweeper.py
## The AI player for the Minesweeper games
## Processes the board and makes the best move it knows based on the
## probabilities.
## Author   : Cameron Taylor
## ID       : cat7641
## Version  : 12/1/2016
from Minesweeper import *
from random import randint


class AIMinesweeper:
   """
   The AI player that solves the minesweeper game
   """
   def __init__(self, game, size, numBombs):
      self.board = game
      self.defaultProb = numBombs/(size*size)
      self.probBoard = [["c" for x in range(0, size)] for y in range(0,size)]
      self.size = size
      self.numBombs = numBombs

   """
   Find the best potential mmoves and randomly chooses one
   """
   def getMove(self):
      minProb = 1.0
      moves = []
      for x in range(0, self.size):
         for y in range(0, self.size):
            ## probability is either the default probability, or the
            ## probability given by the probability board.
            if self.probBoard[x][y] == "c":
               value = self.defaultProb
            else:
               value = self.probBoard[x][y]
            ## If there is a space that is guarenteed to be a bomb, then
            ## flag it, otherwise start adding potential moves to the
            ## list of potential moves. If a new lowest probability is
            ## found, make a new list. If the same probability is found,
            ## then just add it to the existing list.
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

   """
   After making a move and gaining more information, updates its
   knowledge of the board.
   """
   def updateBoard(self, game):
      self.board = game
      self.probBoard = [["c" for x in range(0, self.size)] for y in range(0,self.size)]
      for x in range(0,self.size):
         for y in range(0, self.size):
            ## Keep track of the empty spaces aroung the space being
            ## examined.
            spaces = []
            ## If a space is flagged, then it is automattically assigned
            ## the probability of 1.
            if self.board[x][y] == "F":
               self.probBoard[x][y] = 1.0
            ## process the probability of an unknown space
            elif self.board[x][y] != "X":
               s = 0
               f = 0
               self.probBoard[x][y] = 0.0
               ## if the space has been revealed to be empty, then there
               ## is are 0 mines around it. Other wise it gets the value
               ## show on the space.
               if self.board[x][y] == " ":
                  m = 0
               else:
                  m = self.board[x][y]
               ## Count the number of flagged mines around the space.
               for a in range(max(x-1, 0), min(x+2, self.size)):
                  for b in range(max(y-1,0), min(y+2, self.size)):
                     if self.board[a][b] == "F":
                        f = f + 1
               ## If all mines around a space are flagged, then the
               ## probability of all the empty spaces around the space
               ## having a mine are 0.
               if m-f == 0:
                  for a in range(max(x-1, 0), min(x+2, self.size)):
                     for b in range(max(y-1,0), min(y+2, self.size)):
                        if self.board[a][b] == "X":
                           self.probBoard[a][b] = 0.0
               else:
                  f = 0
                  ## create the list of empty spaces
                  for a in range(max(x-1, 0), min(x+2, self.size)):
                     for b in range(max(y-1,0), min(y+2, self.size)):
                        if self.board[a][b] == "X" and self.probBoard[a][b] != 0.0:
                           spaces.append([a,b])
                           s = s + 1
                        if self.board[a][b] == "F":
                           f = f + 1
                  ## If there are empty spaces to be processed, then for
                  ## each space assign it the new probability of having
                  ## a mine if the probability of it having a mine is
                  ## larger than before.
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
      ##Set the default probability to its new value
      f = 0
      z = 0
      for x in range(0, self.size):
         for y in range(0, self.size):
            if self.board[x][y] == "F":
               f = f + 1
            if self.board[x][y] == "X":
               z = z + 1
      self.defaultProb = (self.numBombs - f)/ z
