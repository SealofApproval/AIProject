class stats:
    def __init__(self):
        self.firstList = []
        self.secondList = []
        self.thirdList = []
        self.fourthList = []

    def add(self, wins, losses, size, numBombs):
        if (numBombs/(size * size)) * 100 < 10:
            self.firstList.append([wins, losses])
        elif (numBombs/(size * size)) * 100 < 20:
            self.secondList.append([wins, losses])
        elif (numBombs/(size * size)) * 100 < 30:
            self.thirdList.append([wins, losses])
        elif (numBombs/(size * size)) * 100 < 40:
            self.fourthList.append([wins,losses])
        else:
            print("No list exists to hold this")

    def printStats(self):
        print("")
        print("______________________________________________")
        print("")
        print("Map bomb %: 0 <= x < 10")
        if len(self.firstList) == 0:
            print("Average success rate: N/A")
        else:
            totalwins = 0
            totalgames = 0
            for i in range(len(self.firstList)):
                totalwins = totalwins + self.firstList[i][0]
                totalgames = totalgames + self.firstList[i][1] + self.firstList[i][0]
            print("Average success rate: " + str((totalwins/totalgames) * 100))
        print("Map bomb %: 10 <= x < 20")
        if len(self.secondList) == 0:
            print("Average success rate: N/A")
        else:
            totalwins = 0
            totalgames = 0
            for i in range(len(self.secondList)):
                totalwins = totalwins + self.secondList[i][0]
                totalgames = totalgames + self.secondList[i][1] + self.secondList[i][0]
            print("Average success rate: " + str((totalwins/totalgames) * 100))
        print("Map bomb %: 20 <= x < 30")
        if len(self.thirdList) == 0:
            print("Average success rate: N/A")
        else:
            totalwins = 0
            totalgames = 0
            for i in range(len(self.thirdList)):
                totalwins = totalwins + self.thirdList[i][0]
                totalgames = totalgames + self.thirdList[i][1] + self.thirdList[i][0]
            print("Average success rate: " + str((totalwins/totalgames) * 100))
        print("Map bomb %: 30 <= x < 40")
        if len(self.fourthList) == 0:
            print("Average success rate: N/A")
        else:
            totalwins = 0
            totalgames = 0
            for i in range(len(self.fourthList)):
                totalwins = totalwins + self.fourthList[i][0]
                totalgames = totalgames + self.fourthList[i][1] + self.fourthList[i][0]
            print("Average success rate: " + str((totalwins/totalgames) * 100))
        print("")
