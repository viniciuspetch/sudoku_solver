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


def backtracking(solution):
    id_count = 0
    solution.id = id_count
    id_count += 1
    solution_stack = [solution]

    while(len(solution_stack) > 0):
        curr_solution = solution_stack.pop()

        nf_x, nf_y = getFirstNonFinal(curr_solution)
        print(nf_x, nf_y)
        print(curr_solution.matrix[nf_x][nf_y].mark)
        if nf_x == -1 and nf_y == -1:
            return curr_solution
        possible = True

        for i in range(9):
            if curr_solution.matrix[nf_x][nf_y].mark[i]:
                # Create copy to modify
                new_solution = copy.deepcopy(curr_solution)
                new_solution.id = id_count
                id_count += 1

                # Print
                print('Errors: %d; Gaps: %d; Non-finals: %d' %
                      (new_solution.countErrors(), new_solution.countGaps(), new_solution.countNonFinal()))
                new_solution.print2()
                new_solution.printShort()

                # Set the first non-final cell as final for each option value
                print("Set (%d,%d) to %d" % (nf_x, nf_y, i+1))
                for j in range(9):
                    new_solution.matrix[nf_x][nf_y].mark[j] = False
                new_solution.matrix[nf_x][nf_y].mark[i] = True
                new_solution.matrix[nf_x][nf_y].isNowFinal()

                # Print
                print('Errors: %d; Gaps: %d; Non-finals: %d' %
                      (new_solution.countErrors(), new_solution.countGaps(), new_solution.countNonFinal()))
                new_solution.print2()
                new_solution.printShort()

                # Apply heuristic
                repeat = True
                while(repeat):
                    repeat = heuristic1(new_solution)

                # Print
                print('Errors: %d; Gaps: %d; Non-finals: %d' %
                      (new_solution.countErrors(), new_solution.countGaps(), new_solution.countNonFinal()))
                new_solution.print2()
                new_solution.printShort()
                print("\n\n")

                # Eliminate dead ends
                possible = True
                for i in range(9):
                    for j in range(9):
                        if curr_solution.matrix[i][j].final != True and curr_solution.matrix[i][j].mark.count(True) == 0 and possible == True:
                            print('ID %d is a dead end' % curr_solution.id)
                            possible = False

                if curr_solution.countErrors() > 0:
                    possible = False

                if possible:
                    solution_stack.append(copy.copy(new_solution))
