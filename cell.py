class Cell:
    def __init__(self, isFixed, value):
        self.fixed = isFixed

        if (self.fixed == True):
            self.final = True
            self.mark = [False for x in range(9)]
            self.mark[value-1] = True
        else:
            self.final = False
            self.mark = [True for x in range(9)]

    def isNowFinal(self):
        if self.final == True:
            return False
        else:
            if (self.mark.count(True) == 1):
                self.final = True
                return True
            else:
                return False
