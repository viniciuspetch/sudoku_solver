from cell import Cell
from solution import Solution
import sys
import copy


def getFirstNonFinal(solution):
    for i in range(9):
        for j in range(9):
            if solution.matrix[i][j].final != True:
                return (i, j)
    return (-1, -1)


def heuristic1(solution):
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


def backtracking(solution, printFlag=True):
    if printFlag:
        print("Backtracking: Start")
    solution_stack = [solution]

    while(len(solution_stack) > 0):
        curr_solution = solution_stack.pop()
        # Check inconsistencies
        if curr_solution.checkInc():
            print("[ERROR] Backtracking: Inconsistency found")

        # Get the first non-final cell
        # Stop
        nf_x, nf_y = getFirstNonFinal(curr_solution)
        if nf_x == -1 and nf_y == -1:
            if printFlag:
                print("Backtracking: Found a complete solution")
                curr_solution.printStats()
                curr_solution.printTableShort()
            return curr_solution

            # Print
            if printFlag:
                print("Backtracking: Solution from stack")
                curr_solution.printStats()
                curr_solution.printTableShort()

        for i in range(9):
            if curr_solution.matrix[nf_x][nf_y].mark[i]:
                # Create copy to modify
                new_solution = copy.deepcopy(curr_solution)

                # Set the first non-final cell as final for each option value
                new_solution.matrix[nf_x][nf_y].setFinal(i+1)

                # Print
                if printFlag:
                    print("Backtracking: Set cell value at (%d,%d) to %d" %
                          (nf_x, nf_y, i+1))
                    new_solution.printStats()
                    new_solution.printTableShort()

                # Apply heuristic
                repeat = True
                while(repeat):
                    repeat = heuristic1(new_solution)

                # Print
                if printFlag:
                    print("Backtracking: Heuristic applied")
                    new_solution.printStats()
                    new_solution.printTableShort()

                # Eliminate dead ends
                possible = True
                if new_solution.countErrors() > 0 or new_solution.countGaps() > 0:
                    possible = False

                if curr_solution.countErrors() > 0:
                    possible = False

                if possible:
                    solution_stack.append(copy.copy(new_solution))
