from cell import Cell


class Solution:
    def __init__(self, instance):
        self.errorQt = 0
        self.matrix = []

        for i in range(9):
            aux_list = []
            for j in range(9):
                if (instance[i][j] == '0'):
                    aux_list.append(Cell(False, -1))
                else:
                    aux_list.append(Cell(True, int(instance[i][j])))
            self.matrix.append(aux_list.copy())

    def print(self):
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
                        if self.matrix[i][j].mark[k] == True:
                            aux_string = aux_string + str(k+1)
                        else:
                            aux_string = aux_string + "-"
                    else:
                        if self.matrix[i][j].mark[k] == True:
                            aux_string = aux_string + str(k+1)
                        else:
                            aux_string = aux_string + " "
            aux_string = aux_string + "||"

            print(aux_string)
        print('='*95)
        print()
