from cell import Cell
from solution import Solution
from algorithms import *
import time
import sys
import copy


def matrixToString(solMatrix):
    solString = ''
    for i in range(9):
        for j in range(9):
            solString += solMatrix[i][j]
        solString += '\n'
    return solString


def stringToMatrix(solString):
    solMatrix = []
    for i in range(9):
        solMatrix.append([])
        for j in range(9):
            solMatrix[i].append(int(solString[j+i*9]))
    return solMatrix


def filterInstance(instString):
    return "".join("".join(c for c in instString if c.isdigit()).split("\n"))


def loadInstance(filename):
    try:
        if filename[-4:] != '.txt':
            filename += '.txt'
    except:
        print("[ERROR] Main: Something wrong when opening the instance")
        sys.exit()
    instance = []
    with open(dir, 'r') as file:
        for i in range(9):
            file_line = file.readline()
            file_line_items = file_line.split(' ')[0:-1]
            instance.append(file_line_items.copy())
    return instance


def main(matrix):
    grid = Solution(matrix)
    grid.printTable()
    grid = backtracking(grid)
    return grid


if __name__ == "__main__":
    instance_filename = ''
    print_flag = 2
    algorithm = 'none'
    for i in range(1, len(sys.argv)):
        if sys.argv[i][0] == '-':
            if sys.argv[i] == '-i' or sys.argv[i] == '-inst' or sys.argv[i] == '-instance':
                instance_filename = sys.argv[i+1]
                i += 1
            elif sys.argv[i] == '-t' or sys.argv[i] == '-time':
                print_flag = -1
            elif sys.argv[i] == '-p0' or sys.argv[i] == '-print0':
                print_flag = 0
            elif sys.argv[i] == '-p1' or sys.argv[i] == '-print1':
                print_flag = 1
            elif sys.argv[i] == '-backtracking' or sys.argv[i] == '-bt':
                algorithm = 'backtracking'
            elif sys.argv[i] == '-estochastic' or sys.argv[i] == '-ebt':
                algorithm = 'estochastic'
    initialSolution = loadInstance(instance_filename)
    main(initialSolution, print_flag, algorithm)
