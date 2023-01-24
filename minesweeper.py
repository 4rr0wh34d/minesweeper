# *******         TASK 28             *******
# *******     Compulsory Task 1       *******
# *******       minesweeper.py        *******
# ---------------  xxx -----------------------
# This program is an example of 2D List where we use logic and index to find the count of certain character
# surrounding an element in 2D list


def count_mines(no_of_mines):
    total_mines = 0
    for mine in no_of_mines:
        if mine == "#":
            total_mines += 1
    return total_mines


# Input to the Program
mines = [["-", "-", "-", "#", "#"],
         ["-", "#", "-", "-", "-"],
         ["-", "-", "#", "-", "-"],
         ["-", "#", "#", "-", "-"],
         ["-", "-", "-", "-", "-"]]

size = len(mines)
surrounding_mines = []

# Printing the input
print("Input :")
for line in mines:
    print(line)

# looping through each row and column
for i, value_row in enumerate(mines):
    for j, value_col in enumerate(value_row):

        if value_col == '-':

            if not i - 1 < 0:
                surrounding_mines.append(mines[i - 1][j])
                if not j - 1 < 0:
                    surrounding_mines.append(mines[i - 1][j - 1])
                if not j + 1 > size - 1:
                    surrounding_mines.append(mines[i - 1][j + 1])
            if not j - 1 < 0:
                surrounding_mines.append(mines[i][j - 1])

            if not j + 1 > size - 1:
                surrounding_mines.append(mines[i][j + 1])

            if not i + 1 > size - 1:
                surrounding_mines.append(mines[i + 1][j])
                if not j - 1 < 0:
                    surrounding_mines.append(mines[i + 1][j - 1])
                if not j + 1 > size - 1:
                    surrounding_mines.append(mines[i + 1][j + 1])

            total_mines_around = count_mines(surrounding_mines)
            mines[i][j] = str(total_mines_around)
            surrounding_mines = []

# Printing the output
print("\nOutput :")
for line in mines:
    print(line)
