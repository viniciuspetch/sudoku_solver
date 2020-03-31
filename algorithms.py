from cell import Cell
from solution import Solution
import sys
import copy
from random import randrange


def getFirstNonFinal(solution):
    for i in range(9):
        for j in range(9):
            if solution.matrix[i][j].final != True:
                return (i, j)
    return (-1, -1)


def getAllNonFinal(solution):
    nf_list = []
    for i in range(9):
        for j in range(9):
            if solution.matrix[i][j].final != True:
                nf_list.append((i, j))
    return nf_list


def runHeuristicGroup(solution):
    repeat = 0
    while repeat < 2:
        if repeat == 0:
            hres = constrProp(solution)
        elif repeat == 1:
            hres = uniqueMentionHeuristic(solution)
        if hres:
            repeat = -1
        repeat += 1


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
                        grid.matrix[k][l].mark[grid.matrix[i][j].value-1] = False
    return grid.checkFinal()


def uniqueMentionHeuristic(solution):
    for i in range(9):
        count = [0 for i in range(9)]
        for j in range(9):
            for k in range(9):
                if solution.matrix[i][j].mark[k]:
                    count[k] += 1
        for j in range(9):
            if count[j] == 1:
                for k in range(9):
                    if solution.matrix[i][k].mark[j] and solution.matrix[i][k].final == False:
                        for l in range(9):
                            solution.matrix[i][k].mark[l] = False
                        solution.matrix[i][k].mark[j] = True
        count = [0 for i in range(9)]
        for j in range(9):
            for k in range(9):
                if solution.matrix[j][i].mark[k]:
                    count[k] += 1
        for j in range(9):
            if count[j] == 1:
                for k in range(9):
                    if solution.matrix[k][i].mark[j] and solution.matrix[k][i].final == False:
                        for l in range(9):
                            solution.matrix[k][i].mark[l] = False
                        solution.matrix[k][i].mark[j] = True
        return solution.checkFinal()

# Iterative backtracking


def backtracking(solution, print_flag=2):
    solution_stack = [solution]
    while(len(solution_stack) > 0):
        curr_solution = solution_stack.pop()
        runHeuristicGroup(curr_solution)
        nf_x, nf_y = getFirstNonFinal(curr_solution)
        if nf_x == -1 and nf_y == -1:
            return curr_solution
        for i in range(9):
            if curr_solution.matrix[nf_x][nf_y].mark[i]:
                new_solution = copy.deepcopy(curr_solution)
                new_solution.matrix[nf_x][nf_y].setFinal(i+1)
                runHeuristicGroup(solution)
                possible = True
                if new_solution.countGaps() > 0:
                    possible = False
                if possible:
                    solution_stack.append(copy.copy(new_solution))
