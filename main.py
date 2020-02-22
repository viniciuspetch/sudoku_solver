from cell import Cell
from solution import Solution
from algorithms import heuristic1, backtracking
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


def main(instance_file_name):
    try:
        if instance_file_name[-4:] != '.txt':
            instance_file_name += '.txt'
        instance = loadInstance(instance_file_name)
    except:
        print("Something wrong when opening the instance")
        sys.exit()
    solution = Solution(instance)

    repeat = True
    print("Main: Instance")
    solution.printTableShort()
    while(repeat):
        repeat = heuristic1(solution)
        if repeat:
            solution.printStats()
    print("Main: First heuristic execution result")
    solution.printTableShort()

    backtracking(solution)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit()
    main(sys.argv[1])
