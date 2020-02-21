from cell import Cell
from solution import Solution

def loadInstance(dir):
    instance = []

    with open(dir, 'r') as file:
        for i in range(9):
            file_line = file.readline()
            file_line_items = file_line.split(' ')[0:-1]
            instance.append(file_line_items.copy())

    return instance


def main():
    instance = loadInstance('s01a.txt')
    solution = Solution(instance)
    solution.print()

    # Start removing conflicts with fixed numbers
    for i in range(9):
        for j in range(9):
            if solution.matrix[i][j].fixed == True:
                # Get value
                value = -1
                for k in range(9):
                    if solution.matrix[i][j].mark[k] == True:
                        value = k
                for k in range(9):
                    if k != i:
                        solution.matrix[k][j].mark[value] = False
                    if k != j:
                        solution.matrix[i][k].mark[value] = False

    solution.print()




if __name__ == "__main__":
    main()
