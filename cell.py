class Cell:
    def __init__(self, isFinal, value):
        self.final = isFinal
        self.value = 0

        if (self.final == True):
            self.mark = [False for x in range(9)]
            self.mark[value-1] = True
            self.value = value
        else:
            self.mark = [True for x in range(9)]

    def isNowFinal(self):
        if self.final == True:
            return False
        else:
            if (self.mark.count(True) == 1):
                self.final = True
                for i in range(9):
                    if self.mark[i] == True:
                        self.value = i+1
                return True
            else:
                return False

    def checkFinal(self):
        if self.final == True:
            return False
        
        if (self.mark.count(True) == 1):
            self.final = True
            for i in range(9):
                if self.mark[i] == True:
                    self.value = i+1
            return True
        else:
            return False

    def setFinal(self, value):
        if self.final == True:
            return False
        for i in range(9):
            self.mark[i] = False
        self.mark[value-1] = True
        self.value = value
        self.final = True
        return True
