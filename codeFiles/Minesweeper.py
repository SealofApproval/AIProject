from random import randint

class Minesweeper:
    def __init__(self, numBombs, size):
        self.size = size
        self.numBombs = numBombs
        self.firstDone = False
        self.emptyNeighbors = []
        self.checked = []
        self.board = [["X" for x in range(0, size)] for y in range(0, size)]
        self.solution = [[0 for x in range(0, size)] for y in range(0, size)]

    def printBoard(self):
        print("  0123456789\n")
        for i in range(0, self.size):
            print(i, end=" ")
            for j in range(0, self.size):
                if j != self.size-1:
                    print(self.board[i][j], end="")
                else:
                    print(self.board[i][j])

    def printSolution(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                if j != self.size-1:
                    print(self.solution[i][j], end="")
                else:
                    print(self.solution[i][j])

    def processSurroundings(self, x, y):
        for i in range(max(x-1, 0), min(x+1, self.size-1)+1):
            for j in range(max(y-1, 0), min(y+1, self.size-1)+1):
                if self.solution[i][j] != -1:
                    self.solution[i][j] = self.solution[i][j] + 1

    def processMove(self, x, y):
        if not self.firstDone:
            self.firstDone = True
            for i in range(0, self.numBombs):
                bx = randint(0, self.size-1)
                by = randint(0, self.size-1)
                if((bx == x and by == y) or self.solution[bx][by] == -1):
                    i = i - 1
                else:
                    self.solution[bx][by] = -1
                    self.processSurroundings(bx, by)
            return self.reveal(x, y)
        else:
            return self.reveal(x, y)

    def reveal(self, x, y):
        if self.solution[x][y] == 0:
            self.board[x][y] = " "
            for i in range(max(x-1, 0), min(x+1, self.size-1)+1):
                for j in range(max(y-1, 0), min(y+1, self.size-1)+1):
                    if([i, j] not in self.checked):
                        self.checked.append([i, j])
                        self.reveal(i, j)
            return True
        elif self.solution[x][y] > 0:
            self.board[x][y] = self.solution[x][y]
            self.checked.append([x, y])
            return True
        else:
            self.board[x][y] = "!"
            return False

    def processFlag(self, x, y):
        if x < 0 or x > self.size - 1:
            if y < 0 or y > self.size - 1:
                return -1
        if self.board[x][y] == "F":
            self.board[x][y] = "X"
            return 0
        if self.board[x][y] != "X":
            return -1
        self.board[x][y] = "F"
        return 0

    def checkWin(self):
        numCorrect = 0
        numFlags = 0
        returnVal = False
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.board[i][j] == "F":
                    numFlags = numFlags + 1
                    if self.board[i][j] == "F" and self.solution[i][j] == -1:
                        numCorrect = numCorrect + 1
        #for some reason the part after the or wasn't correctly triggering. Can add back in with a rework if desired
        #if (numCorrect == self.numBombs and numFlags == self.numBombs) or len(self.checked) == self.size ** 2 - self.numBombs:
        if numCorrect == self.numBombs and numFlags == self.numBombs:
            returnVal = True

        return returnVal
