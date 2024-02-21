import tkinter as tk
from tkinter import messagebox
import numpy as np
import random

puzzle1 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
           [6, 0, 0, 1, 9, 5, 0, 0, 0],
           [0, 9, 8, 0, 0, 0, 0, 6, 0],
           [8, 0, 0, 0, 6, 0, 0, 0, 3],
           [4, 0, 0, 8, 0, 3, 0, 0, 1],
           [7, 0, 0, 0, 2, 0, 0, 0, 6],
           [0, 6, 0, 0, 0, 0, 2, 8, 0],
           [0, 0, 0, 4, 1, 9, 0, 0, 5],
           [0, 0, 0, 0, 8, 0, 0, 7, 9]]
puzzle2 = [[0, 0, 6, 0, 2, 0, 0, 5, 0],
           [0, 0, 2, 0, 0, 0, 1, 9, 4],
           [0, 0, 0, 1, 0, 0, 2, 0, 7],
           [6, 0, 7, 0, 8, 2, 0, 1, 9],
           [0, 8, 5, 0, 7, 0, 0, 3, 0],
           [0, 0, 0, 6, 0, 5, 4, 0, 0],
           [0, 9, 0, 0, 1, 3, 0, 4, 0],
           [0, 0, 1, 0, 0, 9, 0, 0, 0],
           [7, 3, 0, 0, 0, 8, 9, 0, 0]]
puzzle3 = [[0, 4, 6, 0, 0, 0, 0, 0, 0],
           [9, 0, 2, 0, 6, 0, 0, 0, 8],
           [0, 0, 8, 4, 0, 0, 2, 5, 0],
           [0, 0, 0, 8, 0, 0, 0, 7, 0],
           [5, 0, 0, 7, 0, 2, 0, 0, 3],
           [0, 1, 0, 0, 0, 6, 0, 0, 0],
           [0, 6, 4, 0, 0, 3, 9, 0, 0],
           [3, 0, 0, 0, 8, 0, 1, 0, 2],
           [0, 0, 0, 0, 0, 0, 7, 3, 0]]
puzzle4 = [[0, 0, 8, 0, 3, 0, 5, 4, 0],
           [3, 0, 0, 4, 0, 7, 9, 0, 0],
           [4, 1, 0, 0, 0, 8, 0, 0, 2],
           [0, 4, 3, 5, 0, 2, 0, 6, 0],
           [5, 0, 0, 0, 0, 0, 0, 0, 8],
           [0, 6, 0, 3, 0, 9, 4, 1, 0],
           [1, 0, 0, 8, 0, 0, 0, 2, 7],
           [0, 0, 5, 6, 0, 3, 0, 0, 4],
           [0, 2, 9, 0, 7, 0, 8, 0, 0]]
puzzle5 = [[6, 0, 0, 1, 0, 8, 2, 0, 3],
           [0, 2, 0, 0, 4, 0, 0, 9, 0],
           [8, 0, 3, 0, 0, 5, 4, 0, 0],
           [5, 0, 4, 6, 0, 7, 0, 0, 9],
           [0, 3, 0, 0, 0, 0, 0, 5, 0],
           [7, 0, 0, 8, 0, 3, 1, 0, 2],
           [0, 0, 1, 7, 0, 0, 9, 0, 6],
           [0, 8, 0, 0, 3, 0, 0, 2, 0],
           [3, 0, 2, 9, 0, 4, 0, 0, 5]]
puzzle6 = [[6, 0, 5, 7, 2, 0, 0, 3, 9],
           [4, 0, 0, 0, 0, 5, 1, 0, 0],
           [0, 2, 0, 1, 0, 0, 0, 0, 4],
           [0, 9, 0, 0, 3, 0, 7, 0, 6],
           [1, 0, 0, 8, 0, 9, 0, 0, 5],
           [2, 0, 4, 0, 5, 0, 0, 8, 0],
           [8, 0, 0, 0, 0, 3, 0, 2, 0],
           [0, 0, 2, 9, 0, 0, 0, 0, 1],
           [3, 5, 0, 0, 6, 7, 4, 0, 8]]
puzzle7 = [[0, 1, 9, 0, 6, 0, 5, 4, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [8, 2, 0, 9, 7, 4, 0, 3, 6],
           [0, 0, 1, 5, 0, 3, 8, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 2, 7, 0, 1, 6, 0, 0],
           [7, 5, 0, 1, 3, 8, 0, 9, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 8, 3, 0, 4, 0, 7, 1, 0]]


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # main settings of tkinter window
        self.geometry("525x750+500+0")
        self.title("Sudoku solver")

        # definition of 2 frames in the window
        self.top_frame = tk.Frame(self)
        self.top_frame.grid(row=0, column=0)
        self.bot_frame = tk.Frame(self)
        self.bot_frame.grid(row=1, column=0)

        # definition of the label at the top of the window
        self.top_label = tk.Label(self.top_frame, text="What do you want to do?", font=('Arial', 16))
        self.top_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # definition of 2 first buttons in the window
        self.random_btn = tk.Button(self.top_frame, text="Show random puzzle", width=20, height=1, font=('Arial', 16),
                                    command=self.random_puzzle)
        self.random_btn.grid(row=1, column=0, padx=5, pady=5)
        self.own_btn = tk.Button(self.top_frame, text="Input your puzzle", width=20, height=1, font=('Arial', 16),
                                 command=self.own_puzzle)
        self.own_btn.grid(row=1, column=1, padx=5, pady=5)

        # action during exit
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.mainloop()

    def random_puzzle(self):
        """
        Function selects random puzzle from group of predefined puzzles and showing it in the window. Function also
        defines button to pass unsolved puzzle to solving function.
        """
        # cleaning bottom frame of window
        for widget in self.bot_frame.winfo_children():
            widget.destroy()

        # random puzzle selection
        unsolved_list = random.choice([puzzle1, puzzle2, puzzle3, puzzle4, puzzle5, puzzle6, puzzle7])

        # showing random puzzle
        outer_str = ''
        for count_row, row in enumerate(unsolved_list):
            inner_str = ''
            for count_col, x in enumerate(row):
                if count_col in [3, 6]:
                    inner_str += f' :  {x if x != 0 else "  "} '
                else:
                    inner_str += f' {x if x != 0 else "  "} '
            if count_row in [3, 6]:
                outer_str += '\n ..  ..  ..     ..  ..  ..     ..  ..  .. \n' + inner_str
            else:
                outer_str += '\n' + inner_str
        unsolved_str = outer_str + '\n'

        # unsolved_str = '\n'.join(' '.join(str(x) for x in row) for row in unsolved_list)
        unsolved_lab = tk.Label(self.bot_frame, text=unsolved_str, font=('Arial', 14))
        unsolved_lab.grid(row=0, column=0)

        # button which caused passing unsolved puzzle to solving function
        solve_btn = tk.Button(self.bot_frame, text="Solve this puzzle", width=22, font=('Arial', 16),
                              command=lambda: self.solve_puzzle(unsolved_list))
        solve_btn.grid(row=1, column=0, padx=5, pady=5)

    def own_puzzle(self):
        """
        Function shows 9x9 grid of entry boxes in the window. Function defines button to pass users inputs to checking
        function.
        """
        # cleaning bottom frame of window
        for widget in self.bot_frame.winfo_children():
            widget.destroy()

        # 9x9 grid of entry boxes inserted into 2d list
        outer_list_entry = []
        for r in range(9):
            if r in [0, 1, 2]:
                r_pos = r
            elif r in [3, 4, 5]:
                r_pos = r + 1
            else:
                r_pos = r + 2
            inner_list_entry = []
            for c in range(9):
                if c in [0, 1, 2]:
                    c_pos = c
                elif c in [3, 4, 5]:
                    c_pos = c + 1
                else:
                    c_pos = c + 2
                box_entry = tk.Entry(self.bot_frame, width=3, justify='center', font=('Arial', 10))
                box_entry.grid(row=r_pos, column=c_pos, padx=3, pady=3)
                inner_list_entry.append(box_entry)
            outer_list_entry.append(inner_list_entry)

        # gaps between 3x3 grid of entry boxes
        for r in (3, 7):
            for c in (3, 7):
                space_label = tk.Label(self.bot_frame, text=" . ")
                space_label.grid(row=r, column=c)

        # button which caused passing users inputs to checking function
        check_btn = tk.Button(self.bot_frame, text="Check and save your puzzle", width=22, font=('Arial', 16),
                              command=lambda: self.check_puzzle(outer_list_entry))
        check_btn.grid(row=11, column=0, columnspan=11, padx=5, pady=5)

    def check_puzzle(self, outer_list_entry: list):
        """
        Function checks correction of single input, single row, single column and single 3x3 box of inputs. Function
        defines button to pass users inputs to solving function. The button is set in disabled state if users inputs are
        incorrect.
        :param outer_list_entry: 9x9 2d list of tkinter entry objects with sudoku puzzle to solve
        """
        # button which caused passing unsolved puzzle to solving function, setting it to normal state
        solve_btn = tk.Button(self.bot_frame, text="Solve this puzzle", width=22, font=('Arial', 16),
                              command=lambda: self.solve_puzzle(unsolved_list))
        solve_btn.grid(row=12, column=0, columnspan=11, padx=5, pady=5)
        solve_btn['state'] = tk.NORMAL

        # checking correction of single input, saving puzzle if correct input, message and solving button in disable
        # state if incorrect input
        unsolved_list = []
        count_row = 0
        for inner_list_entry in outer_list_entry:
            count_row += 1
            inner_unsolved_list = []
            count_col = 0
            for square_entry in inner_list_entry:
                count_col += 1
                square_str = square_entry.get()
                if square_str in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    inner_unsolved_list.append(int(square_str))
                elif square_str == "":
                    inner_unsolved_list.append(0)
                else:
                    inner_unsolved_list.append(0)
                    mes1 = f"Incorrect input in {count_row} row and {count_col} column.\n" \
                           f"You can input single number from 1 to 9 or leave empty box."
                    messagebox.showerror(title="Incorrect input", message=mes1)
                    solve_btn['state'] = tk.DISABLED
            unsolved_list.append(inner_unsolved_list)

        # checking correction of single row, message if duplicate input in single row
        count_row = 0
        for single_row in unsolved_list:
            count_row += 1
            unique_values = set()
            duplicate_values = []
            for x in single_row:
                if x in unique_values and x != 0:
                    duplicate_values.append(x)
                else:
                    unique_values.add(x)
            if len(duplicate_values) > 0:
                mes2 = f"Duplicated input {str(duplicate_values)[1:-1]} in {count_row} row.\n" \
                       f"Values in the single row can't be duplicated."
                messagebox.showerror(title="Duplicated input in row", message=mes2)
                solve_btn['state'] = tk.DISABLED

        # checking correction of single column, message if duplicate input in single column
        for column_number in range(9):
            single_col = []
            for single_row in unsolved_list:
                single_col.append(single_row[column_number])
            unique_values = set()
            duplicate_values = []
            for x in single_col:
                if x in unique_values and x != 0:
                    duplicate_values.append(x)
                else:
                    unique_values.add(x)
            if len(duplicate_values) > 0:
                mes3 = f"Duplicated input: {str(duplicate_values)[1:-1]} in {column_number + 1} column.\n" \
                       f"Values in the single column can't be duplicated."
                messagebox.showerror(title="Duplicated input in column", message=mes3)
                solve_btn['state'] = tk.DISABLED

        # checking correction of single 3x3 box, message if duplicate input in single 3x3 box
        for box_row in [0, 3, 6]:
            for box_col in [0, 3, 6]:
                single_box = []
                for rr in [0, 1, 2]:
                    for cc in [0, 1, 2]:
                        single_box.append(unsolved_list[rr + box_row][cc + box_col])
                unique_values = set()
                duplicate_values = []
                for x in single_box:
                    if x in unique_values and x != 0:
                        duplicate_values.append(x)
                    else:
                        unique_values.add(x)
                if len(duplicate_values) > 0:
                    mes4 = f"Duplicated input: {str(duplicate_values)[1:-1]} in box: " \
                           f"{box_row + 1}-{box_row + 3} rows and {box_col + 1}-{box_col + 3} columns.\n" \
                           f"Values in the single box can't be duplicated."
                    messagebox.showerror(title="Duplicated input in box", message=mes4)
                    solve_btn['state'] = tk.DISABLED

    def solve_puzzle(self, unsolved_list: list):
        """
        Function solves sudoku puzzle and shows solution in the window. In case of no progress (too many unknowns)
        function breaks and shows message box with warning.
        :param unsolved_list: 9x9 2d list of integers with sudoku puzzle to solve, unknown values as number 0.
        """
        # converting input 2d list with puzzle into 2d numpy array and calculating the number of unknowns
        grid = np.array(unsolved_list)
        # print(f"Puzzle to solve:\n{grid}") ###
        zeros = np.count_nonzero(grid == 0)
        # print(f"Number of unknowns: {zeros}\n") ###

        # loop depending on the remaining number of unknowns
        round_counter = 1
        while zeros > 0:
            # print(f"---Round {round_counter}---") ###

            # loop through every 3x3 box and every value in 9x9 grid, checking if value is in box
            for box_row in [0, 3, 6]:
                for box_col in [0, 3, 6]:
                    for value in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                        box = np.copy(grid[box_row:box_row + 3, box_col:box_col + 3])
                        if value not in box:

                            # loop through every row in 3x3 box and crossing out rows with checking value
                            for square_row in [box_row, box_row + 1, box_row + 2]:
                                if value in grid[square_row, 0:9]:
                                    box[square_row - box_row, :] = [10, 10, 10]

                            # loop through every column in 3x3 box and crossing out columns with checking value
                            for square_col in [box_col, box_col + 1, box_col + 2]:
                                if value in grid[0:9, square_col]:
                                    box[:, square_col - box_col] = [10, 10, 10]

                            # inserting value in the place of unknown if the remaining number of unknowns in 3x3 box
                            # after crossing out is equal to 1
                            if np.count_nonzero(box == 0) == 1:
                                zero_pos = np.argwhere(box == 0)
                                grid[zero_pos[0][0] + box_row, zero_pos[0][1] + box_col] = value
                                # print(f"The value: {value} on the position: {zero_pos[0]}") ###

            # calculating the remaining number of unknowns
            prev_zeros = zeros
            # print(f"Previous number of unknowns: {prev_zeros}") ###
            zeros = np.count_nonzero(grid == 0)
            # print(f"Remaining number of unknowns: {zeros}\n") ###

            # breaking the loop if no progress, probably too many unknowns to have one version of solution/incorrect
            # input
            if prev_zeros == zeros:
                # print(f"No progress, number of unknowns: {zeros}, incorrect input") ###
                messagebox.showerror(title="Incorrect input", message="Too many unknowns")
                break

            round_counter = round_counter + 1

        # solution printing and converting into 2d list
        # print(f"Puzzle solved:\n{grid}") ###
        solved_list = grid
        outer_str = ''
        for count_row, row in enumerate(solved_list):
            inner_str = ''
            for count_col, x in enumerate(row):
                if count_col in [3, 6]:
                    inner_str += f' :  {x if x != 0 else "  "} '
                else:
                    inner_str += f' {x if x != 0 else "  "} '
            if count_row in [3, 6]:
                outer_str += '\n ..  ..  ..     ..  ..  ..     ..  ..  .. \n' + inner_str
            else:
                outer_str += '\n' + inner_str
        solved_str = outer_str

        # solved_list = list(grid)   # why not: solved_list = grid.tolist() ? as np array: solved_list = grid also works
        # solved_str = '\n'.join(' '.join(str(x) for x in row) for row in solved_list)
        solved_lab = tk.Label(self.bot_frame, text=solved_str, font=('Arial', 14))
        solved_lab.grid(row=13, column=0, columnspan=11, padx=5, pady=5)

    def on_closing(self):
        """
        Function showing messagebox with question about exit, activated after pressing exit button.
        """
        # messagebox before exit
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.destroy()
