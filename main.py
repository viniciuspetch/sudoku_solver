from cell import Cell
from solution import Solution
from algorithms import *
import time
import sys
import copy


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


def main(initialSolution, print_flag=-1, algorithm='backtracking'):
    solution = Solution(initialSolution)
    start_time = time.time()
    
    if print_flag >= 2:
        print("Main: Instance")
        solution.printTableShort()

    # Heuristics
    runHeuristicGroup(solution)
    # Check if heuristics already found a final solution
    nf_x, nf_y = getFirstNonFinal(solution)
    if nf_x == -1 and nf_y == -1:
        if print_flag >= 2:
            print("Main: Found a complete solution")
            best_solution = solution
    else:
        if algorithm == 'backtracking':
            if print_flag >= 2:
                print("Main: Using backtracking algorithm")
            best_solution = backtracking(solution, print_flag)
        elif algorithm == 'estochastic':
            if print_flag >= 2:
                print("Main: Using estochastic backtracking algorithm")
            best_solution = estochasticBacktracking(solution, print_flag)
        else:
            if print_flag >= 2:
                print("Main: Using no algorithm")
            best_solution = solution
    if print_flag >= 1:
        best_solution.printStats()
    if print_flag >= 0:
        best_solution.printTableShort()
        print(time.time()-start_time)
    return best_solution


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
