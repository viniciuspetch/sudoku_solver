from cell import Cell
from solution import Solution
import sys
import copy
from random import randrange


def getFirstNonFinal(solution):
    for i in range(9):
        for j in range(9):
            if not solution.matrix[i][j].value:
                return (i, j)
    return (-1, -1)


def getAllNonFinal(solution):
    nf_list = []
    for i in range(9):
        for j in range(9):
            if solution.matrix[i][j].final != True:
                nf_list.append((i, j))
    return nf_list


def constrProp(grid):
    # Constraint Propagation
    for i in range(9):
        for j in range(9):
            if grid.matrix[i][j].value:
                for k in range(9):
                    grid.matrix[k][j].mark[grid.matrix[i][j].value-1] = False
                    grid.matrix[i][k].mark[grid.matrix[i][j].value-1] = False
                for k in range(int(i / 3)*3, int(i / 3)*3+3):
                    for l in range(int(j / 3)*3, int(j / 3)*3+3):
                        grid.matrix[k][l].mark[grid.matrix[i]
                                               [j].value-1] = False
    return grid.checkFinal()


def uniqueMention(solution):
    # Unique Mention
    for i in range(9):
        count1 = [0 for x in range(9)]
        count2 = [0 for x in range(9)]
        for j in range(9):
            for k in range(9):
                if solution.matrix[i][j].mark[k]:
                    count1[k] += 1
                if solution.matrix[j][i].mark[k]:
                    count2[k] += 1
            if solution.matrix[i][j].value:
                count1[solution.matrix[i][j].value-1] += 1
            if solution.matrix[j][i].value:
                count2[solution.matrix[j][i].value-1] += 1
        for j in range(9):
            if count1[j] == 1:
                for k in range(9):
                    if solution.matrix[i][k].mark[j]:
                        solution.matrix[i][k].mark = [False for l in range(9)]
                        solution.matrix[i][k].mark[j] = True
            if count2[j] == 1:
                for k in range(9):
                    if solution.matrix[k][i].mark[j]:
                        solution.matrix[k][i].mark = [False for l in range(9)]
                        solution.matrix[k][i].mark[j] = True
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            count = [0 for x in range(9)]
            for k in range(i, i+3):
                for l in range(j, j+3):
                    for m in range(9):
                        if solution.matrix[k][l].mark[m]:
                            count[m] += 1
                    if solution.matrix[k][l].value:
                        count[solution.matrix[k][l].value-1] += 1
            for k in range(9):
                if count[k] == 1:
                    for l in range(i, i+3):
                        for m in range(j, j+3):
                            if solution.matrix[l][m].mark[k]:
                                solution.matrix[l][m].mark = [
                                    False for o in range(9)]
                                solution.matrix[l][m].mark[k] = True
    return solution.checkFinal()


def backtracking(grid):
    # Iterative backtracking
    gridStack = [grid]
    while(len(gridStack) > 0):
        print("New grid")
        currGrid = gridStack.pop()
        currGrid.printTable()
        repeat = True
        while repeat:
            r1 = constrProp(currGrid)
            print("Constraint Propagation")
            currGrid.printTable()
            r2 = uniqueMention(currGrid)
            print("Unique Mention")
            currGrid.printTable()
            repeat = r1 or r2
        currGrid.printTable()
        if not currGrid.countGaps():
            nf_x, nf_y = getFirstNonFinal(currGrid)
            print(nf_x, nf_y)
            if nf_x == -1 and nf_y == -1:
                return currGrid
            for i in range(9):
                if currGrid.matrix[nf_x][nf_y].mark[i]:
                    newGrid = copy.deepcopy(currGrid)
                    newGrid.matrix[nf_x][nf_y].value = i+1
                    newGrid.matrix[nf_x][nf_y].mark = [False for j in range(9)]
                    gridStack.append(copy.deepcopy(newGrid))
