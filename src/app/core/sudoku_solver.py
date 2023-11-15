import numpy as np


def sudoku(puzzle: list) -> list:
    """
    Function solving sudoku puzzle.
    :param puzzle: 9x9 2d list of integers with sudoku puzzle to solve, unknown values as number 0
    :return: 9x9 2d list of integers with solved sudoku puzzle
    """

    # converting input 2d list with puzzle into 2d numpy array and calculating the number of unknowns
    grid = np.array(puzzle)
    print(f"Puzzle to solve:\n{grid}")
    zeros = np.count_nonzero(grid == 0)
    print(f"Number of unknowns: {zeros}\n")

    # loop depending on the remaining number of unknowns
    round_counter = 1
    while zeros > 0:
        print(f"---Round {round_counter}---")

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
                            print(f"The value: {value} on the position: {zero_pos[0]}")

        # calculating the remaining number of unknowns
        zeros = np.count_nonzero(grid == 0)
        print(f"Remaining number of unknowns: {zeros}\n")
        round_counter = round_counter + 1

    # solution printing and converting into 2d list
    print(f"Puzzle solved:\n{grid}")
    return grid.tolist()
