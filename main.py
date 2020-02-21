from cell import Cell
from solution import Solution
import sys


def loadInstance(dir):
    instance = []

    with open(dir, 'r') as file:
        for i in range(9):
            file_line = file.readline()
            file_line_items = file_line.split(' ')[0:-1]
            instance.append(file_line_items.copy())

    return instance


def firstStep(solution):
    repeat = False

    # Start removing conflicts with fixed numbers
    for i in range(9):
        for j in range(9):
            if solution.matrix[i][j].final == True:
                # Get value
                value = -1
                for k in range(9):
                    if solution.matrix[i][j].mark[k] == True:
                        value = k
                # Clean rows and columns
                for k in range(9):
                    if k != i:
                        solution.matrix[k][j].mark[value] = False
                    if k != j:
                        solution.matrix[i][k].mark[value] = False
                # Clean quadrants
                # print(str(i) + ' '+str(j) + ' / ' +
                      # str(int(i / 3)) + ' ' + str(int(j / 3)))
                for k in range(int(i / 3)*3, int(i / 3)*3+3):
                    for l in range(int(j / 3)*3, int(j / 3)*3+3):
                        #print(str(k) + " " + str(l))
                        if k != i and l != j:
                            solution.matrix[k][l].mark[value] = False

    for i in range(9):
        for j in range(9):
            if (solution.matrix[i][j].isNowFinal() == True):
                #print("(%d, %d) is now final" % (i, j))
                repeat = True

    return repeat


def main(instance_file_name):
    try:
        if instance_file_name[-4:] != '.txt':
            instance_file_name += '.txt'
        instance = loadInstance(instance_file_name)
    except:
        print("Something wrong when opening the instance")
        sys.exit()
    solution = Solution(instance)
    solution.print()
    solution.printFinal()

    repeat = True
    while(repeat):
        repeat = firstStep(solution)
        if (repeat):
            # solution.print()
            solution.printFinal()
    solution.collisionCheck()


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit()
    main(sys.argv[1])
