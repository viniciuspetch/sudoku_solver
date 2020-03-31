from cell import Cell


class Solution:
    def __init__(self, instance):
        self.matrix = [[Cell(instance[i][j]) for i in range(9)]
                       for j in range(9)]

    def toMatrix(self):
        return [[self.matrix[j][i].value for j in range(9)] for i in range(9)]

    def printTable(self):
        for i in range(9):
            aux_string = ""
            for j in range(9):
                if self.matrix[j][i].value:
                    aux_string += "|" + str(self.matrix[j][i].value) + "          "
                else:
                    aux_string += "|  "
                    for k in range(9):
                        if self.matrix[j][i].mark[k]:
                            aux_string += str(k+1)
                        else:
                            aux_string += ' '
            aux_string += "|"
            print(aux_string)
        print()

    def printTableShort(self):
        for i in range(9):
            for j in range(9):
                if self.matrix[j][i].value:
                    print(self.matrix[j][i].value, end=" ")
                else:
                    print(' ', end=" ")
            print()

    def checkFinal(self):
        result = False
        for i in range(9):
            for j in range(9):
                if self.matrix[i][j].checkFinal():
                    result = True
        return result

    def checkSingleFinal(self):
        for i in range(9):
            for j in range(9):
                if self.matrix[i][j].checkFinal():
                    return True
        return False

    def countErrors(self):
        error_qt_x = 0
        error_qt_y = 0
        error_qt_group = 0
        for i in range(9):
            number_count_x = [0 for x in range(9)]
            number_count_y = [0 for x in range(9)]
            for j in range(9):
                for k in range(9):
                    if self.matrix[i][j].final == True and self.matrix[i][j].mark[k] == True:
                        number_count_x[k] += 1
                    if self.matrix[j][i].final == True and self.matrix[j][i].mark[k] == True:
                        number_count_y[k] += 1
            for j in range(9):
                if number_count_x[j] > 1:
                    # print('Error at row %d' % i)
                    error_qt_x += 1
                if number_count_y[j] > 1:
                    # print('Error at column %d' % i)
                    error_qt_y += 1

        for i in range(3):
            for j in range(3):
                number_count_group = [0 for x in range(9)]
                for k in range(i*3, i*3+3):
                    for l in range(j*3, j*3+3):
                        for m in range(9):
                            if self.matrix[k][l].final == True and self.matrix[k][l].mark[m] == True:
                                number_count_group[m] += 1
                for k in range(9):
                    if number_count_group[k] > 1:
                        # print('Error at group (%d,%d)' % (i, j))
                        error_qt_group += 1

        error_qt_total = error_qt_x + error_qt_y + error_qt_group
        # print('(%d, %d, %d) = %d' %
        #   (error_qt_x, error_qt_y, error_qt_group, error_qt_total))
        return error_qt_total

    def countGaps(self):
        count = 0
        for i in range(9):
            for j in range(9):
                if not self.matrix[i][j].value and not self.matrix[i][j].mark.count(True):
                    count += 1
        return count

    def countNonFinal(self):
        gap_qt = 0
        for i in range(9):
            for j in range(9):
                if self.matrix[i][j].final == 0:
                    gap_qt += 1
        return gap_qt

    def printStats(self):
        print('Errors: %d; Gaps: %d; Non-finals: %d' %
              (self.countErrors(), self.countGaps(), self.countNonFinal()))

    def checkInc(self):
        for i in range(9):
            for j in range(9):
                if self.matrix[i][j].final:
                    if self.matrix[i][j].mark.count(True) != 1:
                        return True
                elif self.matrix[i][j].mark.count(True) == 1:
                    return True
        return False
