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
            hres = eliminationProcessHeuristic(solution)
        elif repeat == 1:
            hres = uniqueMentionHeuristic(solution)
        if hres:
            repeat = -1
        repeat += 1


def eliminationProcessHeuristic(solution):
    # First heuristic, deterministic, remove invalid options
    # Returns True if a new cell has a final value, returns False otherwise
    for i in range(9):
        for j in range(9):
            # If a value is final, use as pivot to remove invalid options
            if solution.matrix[i][j].final == True:
                # Get its value
                value = solution.matrix[i][j].value
                # Clean rows and columns
                for k in range(9):
                    if k != i:
                        solution.matrix[k][j].mark[value-1] = False
                    if k != j:
                        solution.matrix[i][k].mark[value-1] = False
                # Clean groups
                for k in range(int(i / 3)*3, int(i / 3)*3+3):
                    for l in range(int(j / 3)*3, int(j / 3)*3+3):
                        if k != i and l != j:
                            solution.matrix[k][l].mark[value-1] = False
    # Update final status of all cells
    return solution.checkFinal()


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


def estochasticBacktracking(solution, print_flag=2):
    if print_flag >= 2:
        print("Estochastic backtracking: Start")
    solution_stack = [solution]

    while(len(solution_stack) > 0):
        curr_solution = solution_stack.pop()
        # Check inconsistencies
        if curr_solution.checkInc():
            print("[ERROR] Estochastic backtracking: Inconsistency found")

        # Get the first non-final cell
        # Stop
        nf_list = getAllNonFinal(curr_solution)

        if len(nf_list) != 0:
            random_cell = randrange(len(nf_list))
            nf_x, nf_y = nf_list[random_cell]
        else:
            if print_flag >= 2:
                print("Estochastic backtracking: Found a complete solution")
                curr_solution.printStats()
                curr_solution.printTableShort()
            return curr_solution

        # Print
        if print_flag >= 2:
            print("Estochastic backtracking: Solution from stack")
            curr_solution.printStats()
            curr_solution.printTableShort()

        for i in range(9):
            if curr_solution.matrix[nf_x][nf_y].mark[i]:
                # Create copy to modify
                new_solution = copy.deepcopy(curr_solution)

                # Set the first non-final cell as final for each option value
                new_solution.matrix[nf_x][nf_y].setFinal(i+1)

                # Print
                if print_flag >= 2:
                    print("Estochastic backtracking: Set cell value at (%d,%d) to %d" %
                          (nf_x, nf_y, i+1))
                    new_solution.printStats()
                    new_solution.printTableShort()

                # Apply heuristic
                repeat = True
                while(repeat):
                    repeat = eliminationProcessHeuristic(new_solution)

                # Print
                if print_flag >= 2:
                    print("Estochastic backtracking: Heuristic applied")
                    new_solution.printStats()
                    new_solution.printTableShort()

                # Eliminate dead ends
                possible = True
                if new_solution.countErrors() > 0:
                    if print_flag >= 2:
                        print(
                            "Estochastic backtracking: Dead end - solution has errors")
                    possible = False
                if new_solution.countGaps() > 0:
                    if print_flag >= 2:
                        print(
                            "Estochastic backtracking: Dead end - solution has gaps")
                    possible = False

                if possible:
                    solution_stack.append(copy.copy(new_solution))


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
