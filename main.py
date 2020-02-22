from cell import Cell
from solution import Solution
from algorithms import backtracking, estochasticBacktracking, heuristic1
import time
import sys
import copy


def loadInstance(dir):
    instance = []

    with open(dir, 'r') as file:
        for i in range(9):
            file_line = file.readline()
            file_line_items = file_line.split(' ')[0:-1]
            instance.append(file_line_items.copy())

    return instance


def main(instance_file_name, printFlag):
    try:
        if instance_file_name[-4:] != '.txt':
            instance_file_name += '.txt'
        instance = loadInstance(instance_file_name)
    except:
        print("Something wrong when opening the instance")
        sys.exit()
    solution = Solution(instance)
    start_time = time.time()

    repeat = True
    if printFlag:
        print("Main: Instance")
        solution.printTableShort()
    while(repeat):
        repeat = heuristic1(solution)
        if repeat and printFlag:
            solution.printStats()
    if printFlag:
        print("Main: First heuristic execution result")
    # solution.printTableShort()

    # best_solution = backtracking(solution, printFlag)
    best_solution = estochasticBacktracking(solution, printFlag)
    best_solution.printStats()
    best_solution.printTableShort()
    print(time.time()-start_time)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()
    arg2 = False
    if len(sys.argv) == 3:
        if sys.argv[2].lower() == 'true':
            arg2 = True
    main(sys.argv[1], arg2)
