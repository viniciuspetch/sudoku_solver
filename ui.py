from tkinter import *
from tkinter.ttk import *
import main

def solveBtnAction():
    statusLabelVar.set("Solving...")
    root.update()
    solve()

def solve():    
    solution = []
    for i in range(9):
        solution.append([])
        for j in range(9):
            if scell[i][j].get() == '':
                solution[i].append('0')
            else:
                solution[i].append(scell[i][j].get())
    result = main.main(solution, algorithm=algoCombobox.get()).toMatrix()
    for i in range(9):
        for j in range(9):
            scell[i][j].delete(0, END)
            scell[i][j].insert(0, result[i][j])
    statusLabelVar.set("Solved!")


root = Tk()
frame1 = Frame(root)
frame1.grid(column=0, row=0)
scell = []
for i in range(9):
    scell.append([])
    for j in range(9):
        scell[i].append(Entry(frame1, width='4'))
        scell[i][j].grid(column=i, row=j)
solveBtn = Button(frame1, text="Solve", command=solveBtnAction)
solveBtn.grid(column=0, row=9, columnspan=3)
statusLabelVar = StringVar()
statusLabel = Label(frame1, textvariable=statusLabelVar)
statusLabel.grid(column=0, row=10, columnspan=4)
algoCombobox = Combobox(frame1, state='readonly')
algoCombobox.grid(column=3, row=9, columnspan=5)
algoCombobox['values'] = ('backtracking', 'estochastic')
algoCombobox.current(0)
root.mainloop()