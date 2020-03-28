from cell import Cell


class Solution:
    def __init__(self, instance):
        self.errorQt = 0
        self.matrix = []
        self.id = -1

        for i in range(9):
            aux_list = []
            for j in range(9):
                if (instance[i][j] == '0'):
                    aux_list.append(Cell(False, -1))
                else:
                    aux_list.append(Cell(True, int(instance[i][j])))
            self.matrix.append(aux_list.copy())

    def toMatrix(self):
        m = []
        for i in range(9):
            m.append([])
            for j in range(9):
                m[i].append(self.matrix[i][j].value)
        return m

    def printTable(self):
        for i in range(9):
            if (i % 3 == 0):
                print('='*95)
            aux_string = ""
            for j in range(9):
                aux_string = aux_string + "|"
                if (j % 3 == 0):
                    aux_string = aux_string + "|"

                for k in range(9):
                    if self.matrix[i][j].fixed == True:
                        sep = '_'
                        if self.matrix[i][j].mark[k] == True:
                            aux_string = aux_string + str(k+1)
                        else:
                            aux_string = aux_string + sep
                    else:
                        sep = ' '
                        if self.matrix[i][j].mark.count(True) == 1:
                            sep = '_'
                        if self.matrix[i][j].mark[k] == True:
                            aux_string = aux_string + str(k+1)
                        else:
                            aux_string = aux_string + sep
            aux_string = aux_string + "||"

            print(aux_string)
        print('='*95)

    def printTableShort(self):
        for i in range(9):
            for j in range(9):
                if self.matrix[i][j].final:
                    print(self.matrix[i][j].value, end=" ")
                else:
                    print('_', end=" ")
            print()

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

    def checkFinal(self):
        new_final = False
        for i in range(9):
            for j in range(9):
                if self.matrix[i][j].checkFinal():
                    new_final = True
        return new_final

    def countGaps(self):
        gap_qt = 0
        for i in range(9):
            for j in range(9):
                if self.matrix[i][j].mark.count(True) == 0:
                    gap_qt += 1
        return gap_qt

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

