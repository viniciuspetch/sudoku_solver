class Cell:
    def __init__(self, value):
        self.value = value
        self.mark = [not bool(self.value) for x in range(9)]

    def isNowFinal(self):
        if self.value:
            return False
        else:
            if self.mark.count(True) == 1:
                for i in range(9):
                    if self.mark[i] == True:
                        self.value = i+1
                return True
            else:
                return False

    def checkFinal(self):
        if self.value:
            return False
        if self.mark.count(True) == 1:
            self.value = self.mark.index(True)+1
            self.mark = [False for j in range(9)]
            return True
        else:
            return False

    def setFinal(self, value):
        if self.value:
            return False
        for i in range(9):
            self.mark[i] = False
        self.value = value
        return True
