import tkinter as tk
from tkinter import messagebox

from src.app.core.sudoku_solver import sudoku
from src.app.core.random_sample_puzzle import random_puzzle


class SudokuGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("600x400+50+50")
        self.root.title("Sudoku solver")

        self.label = tk.Label(self.root, text="What do you want to do?", font=('Arial', 18))
        self.label.grid(row=0, column=0, columnspan=2, padx=0, pady=0)

        self.randombtn = tk.Button(self.root, text="Show random puzzle", font=('Arial', 18), command=self.show_random)
        self.randombtn.grid(row=1, column=0, padx=10, pady=10)

        # self.ownbtn = tk.Button(self.root, text="Input own puzzle", font=('Arial', 18), command=self.input_own)
        # self.ownbtn.grid(row=2, column=0, padx=10, pady=10)

        self.solvebtn = tk.Button(self.root, text="Solve this puzzle", font=('Arial', 18), command=self.solve_puzzle)
        self.solvebtn.grid(row=1, column=1, rowspan=2, padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def show_random(self):
        self.puzzle_list = random_puzzle()
        unsolved_str = '\n'.join(' '.join(str(x) for x in row) for row in self.puzzle_list)
        self.unsolved = tk.Label(self.root, text=unsolved_str, font=('Arial', 16))
        self.unsolved.grid(row=3, column=0, padx=10, pady=10)

    # def input_own(self):
    #     self.ownbox = tk.Text(self.root, height=9, width=9, font=('Arial', 16))
    #     self.ownbox.grid(row=3, column=0, padx=10, pady=10)

    def solve_puzzle(self):
        self.solution = sudoku(self.puzzle_list)
        solved_str = '\n'.join(' '.join(str(x) for x in row) for row in self.solution)
        self.solved = tk.Label(self.root, text=solved_str, font=('Arial', 16))
        self.solved.grid(row=3, column=1, padx=10, pady=10)

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()


SudokuGUI()
