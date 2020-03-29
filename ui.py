import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import main

def transformInstance(instOrig):
    #instString = "".join("".join("".join(c for c in instOrig if c.isdigit()).split()).split("\n"))
    instString = "".join("".join(c for c in instOrig if c.isdigit()).split("\n"))
    instMatrix = []
    for i in range(9):
        instMatrix.append([])
        for j in range(9):
            instMatrix[i].append(int(instString[j+i*9]))
    return instMatrix

def solve():    
    solution = []
    for i in range(9):
        solution.append([])
        for j in range(9):
            if scell[i][j].get() == '':
                solution[i].append('0')
            else:
                scell[i][j]['background'] = 'light grey'
                solution[i].append(scell[i][j].get())
    root.update()
    result = main.main(solution, print_flag=2, algorithm=algoCombobox.get()).toMatrix()
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
        instMatrix = transformInstance(inputFile.read())
        for i in range(9):
            for j in range(9):
                scell[j][i].delete(0, tk.END)
                if instMatrix[i][j] != 0:
                    scell[j][i].insert(0, instMatrix[i][j])
        statusLabelVar.set("File opened")

def outputFileBtnAction():
    filename = filedialog.asksaveasfilename(initialdir="./", title="Select file")
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
        scell[i][j].grid(column=i%3, row=j%3)

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

outputFileBtn = tk.Button(frame2, text="Save file", command=outputFileBtnAction)
outputFileBtn.grid(column=1, row=3, sticky='w')

root.mainloop()