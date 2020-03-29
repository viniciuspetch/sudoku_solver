import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import main


def gridToMatrix():
    solMatrix = []
    for i in range(9):
        solMatrix.append([])
        for j in range(9):
            if scell[i][j].get() == '':
                solMatrix[i].append(0)
            else:
                solMatrix[i].append(int(scell[i][j].get()))
    return solMatrix


def matrixToGrid(solMatrix):
    for i in range(9):
        for j in range(9):
            scell[j][i].delete(0, tk.END)
            if int(solMatrix[i][j]) != 0:
                scell[j][i].insert(0, solMatrix[i][j])


def solve():
    for i in range(9):
        for j in range(9):
            if scell[i][j].get() != '':
                scell[i][j]['background'] = 'light grey'
    root.update()
    result = main.main(gridToMatrix(), print_flag=2,
                       algorithm=algoCombobox.get()).toMatrix()
    for i in range(9):
        for j in range(9):
            scell[i][j].delete(0, tk.END)
            scell[i][j].insert(0, result[i][j])
    statusLabelVar.set("Solved!")


def solveBtnAction():
    statusLabelVar.set("Solving...")
    root.update()
    solve()


def inputFileBtnAction():
    filename = filedialog.askopenfilename(initialdir="./", title="Select file")
    with open(filename, "r") as inputFile:
        matrixToGrid(main.stringToMatrix(main.filterInstance(inputFile.read())))
        statusLabelVar.set("File opened")


def outputFileBtnAction():
    filename = filedialog.asksaveasfilename(
        initialdir="./", title="Select file")
    with open(filename, "w") as outputFile:
        output = ''
        for i in range(9):
            for j in range(9):
                output += scell[j][i].get()
            output += '\n'
        outputFile.write(output)
        statusLabelVar.set("File saved")


root = tk.Tk()
mainframe = tk.Frame(root)
mainframe.grid(column=0, row=0)
frame1 = tk.Frame(mainframe)
frame2 = tk.Frame(mainframe)
frame1.grid(column=0, row=0, sticky='w')
frame2.grid(column=0, row=1, sticky='w')

group = []
for i in range(3):
    group.append([])
    for j in range(3):
        group[i].append(ttk.Labelframe(frame1))
        group[i][j].grid(column=i, row=j)

scell = []
for i in range(9):
    scell.append([])
    for j in range(9):
        scell[i].append(tk.Entry(group[int(i/3)][int(j/3)], width='4'))
        scell[i][j].grid(column=i % 3, row=j % 3)

statusLabelVar = tk.StringVar()
statusLabelVar.set("Idle")
statusLabel = tk.Label(frame2, textvariable=statusLabelVar)
statusLabel.grid(column=0, row=0, sticky='w')

solveBtn = tk.Button(frame2, text="Solve", command=solveBtnAction)
solveBtn.grid(column=0, row=1, sticky='w')

algoCombobox = ttk.Combobox(frame2, state='readonly')
algoCombobox.grid(column=0, row=2, sticky='w')
algoCombobox['values'] = ('backtracking', 'estochastic', 'none')
algoCombobox.current(0)

inputFileBtn = tk.Button(frame2, text="Open file", command=inputFileBtnAction)
inputFileBtn.grid(column=0, row=3, sticky='w')

outputFileBtn = tk.Button(frame2, text="Save file",
                          command=outputFileBtnAction)
outputFileBtn.grid(column=1, row=3, sticky='w')

root.mainloop()
