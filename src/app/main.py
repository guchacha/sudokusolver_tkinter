import tkinter as tk
from tkinter import messagebox

from src.app.core.sudoku_solver import sudoku
from src.app.core.random_sample_puzzle import random_puzzle


def show_random():
    global puzzle_list
    puzzle_list = random_puzzle()
    unsolved_str = '\n'.join(' '.join(str(x) for x in row) for row in puzzle_list)
    unsolved = tk.Label(root, text=unsolved_str, font=('Arial', 18))
    unsolved.grid(row=3, column=0, rowspan=9, columnspan=9, padx=10, pady=10)


def input_own():
    global rl
    rl = []
    for r in range(9):
        cl=[]
        for c in range(9):
            e = tk.Entry(root, width=3)
            e.grid(row=r+3, column=c, pady=3)
            cl.append(e)
        rl.append(cl)
    checkbtn = tk.Button(root, text="Check your puzzle", width=18, font=('Arial', 18), command=checkpuzzle)
    checkbtn.grid(row=12, column=0, columnspan=9, padx=0, pady=5)


def checkpuzzle():
    global puzzle_list
    rowlist = []
    countrow = 0
    for cl in rl:
        countrow += 1
        collist = []
        countcol = 0
        for e in cl:
            countcol += 1
            estr = e.get()
            if estr in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                collist.append(int(estr))
            elif estr == "":
                collist.append(0)
            else:
                messagebox.showerror(title="Incorrect input", message=f"Incorrect input in {countrow} row "
                                                                      f"and {countcol} column.\nYou can input single "
                                                                      f"number from 1 to 9 or leave empty box.")
        rowlist.append(collist)
    puzzle_list = rowlist


def solve_puzzle():
    solution = sudoku(puzzle_list)
    solved_str = '\n'.join(' '.join(str(x) for x in row) for row in solution)
    solved = tk.Label(root, text=solved_str, font=('Arial', 18))
    solved.grid(row=3, column=9, rowspan=9, columnspan=9, padx=10, pady=10)


def on_closing():
    if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
        root.destroy()


root = tk.Tk()

root.geometry("560x500+100+100")
root.title("Sudoku solver")

label = tk.Label(root, text="What do you want to do?", font=('Arial', 18))
label.grid(row=0, column=0, columnspan=17, padx=0, pady=5)

randombtn = tk.Button(root, text="Show random puzzle", width=18, height=1, font=('Arial', 18), command=show_random)
randombtn.grid(row=1, column=0,  columnspan=9, padx=0, pady=5)

ownbtn = tk.Button(root, text="Input own puzzle", width=18, font=('Arial', 18), command=input_own)
ownbtn.grid(row=2, column=0, columnspan=9, padx=0, pady=5)

solvebtn = tk.Button(root, text="Solve this puzzle", width=20, height=2, font=('Arial', 18), command=solve_puzzle)
solvebtn.grid(row=1, column=9, columnspan=9, rowspan=2, padx=0, pady=5)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
