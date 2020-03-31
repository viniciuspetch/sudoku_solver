from cell import Cell
from solution import Solution
from algorithms import *
import time
import sys
import copy


def matrixToString(matrix):
    string = ''
    for i in range(9):
        for j in range(9):
            string += matrix[i][j]
        string += '\n'
    return string


def stringToMatrix(string):
    matrix = []
    for i in range(9):
        matrix.append([])
        for j in range(9):
            matrix[i].append(int(string[j+i*9]))
    return matrix


def filterInstance(instString):
    return "".join("".join(c for c in instString if c.isdigit()).split("\n"))


def loadInstance(filename):
    with open(filename, 'r') as file:
        return stringToMatrix(filterInstance(file.read()))


def main(matrix):
    start = time.time()
    grid = Solution(matrix)
    grid = backtracking(grid)
    end = time.time()
    print(end - start)
    return grid


if __name__ == "__main__":
    for i in range(1, len(sys.argv)):
        instFilename = sys.argv[1]
    initMatrix = loadInstance(instFilename)
    main(initMatrix)
