class Cell:
    def __init__(self, isFixed, value):
        self.fixed = isFixed

        if (self.fixed == True):
            self.mark = [False for x in range(9)]
            self.mark[value-1] = True
        else:
            self.mark = [True for x in range(9)]