import numpy as np


def load_file(file_input):
    res = []
    for line in file_input:
        cur = []
        current_line = line.strip('\n')

        for i in range(len(current_line)):
            cur.append(int(current_line[i]))
        res.append(cur)

    return np.array(res)


def find_right(matrix_input, row, column):
    # take maximum of left elements
    maximum = max(matrix_input[row][:column])

    if matrix_input[row][column] > maximum:
        return True
    else:
        return False


def find_left(matrix_input, row, column):
    # take maximum of right elements
    maximum = max(matrix_input[row][column + 1:])

    if matrix_input[row][column] > maximum:
        return True
    else:
        return False


def find_bottom(matrix_input, row, column):
    # take maximum of below elements
    maximum = max(matrix_input[row + 1:, column])

    if matrix_input[row][column] > maximum:
        return True
    else:
        return False


def find_top(matrix_input, row, column):
    # take maximum of above elements
    maximum = max(matrix_input[:row:, column])

    if matrix_input[row][column] > maximum:
        return True
    else:
        return False


def one(matrix_input):
    inner_trees = 0

    for i in range(1, len(matrix_input) - 1):
        for j in range(1, len(matrix_input[i]) - 1):
            if find_left(matrix_input, i, j) or find_right(matrix_input, i, j) or \
                    find_bottom(matrix_input, i, j) or find_top(matrix_input, i, j):
                inner_trees += 1

    outer_trees = len(matrix_input) * 2 + (len(matrix_input) - 2) * 2

    return inner_trees + outer_trees


def view_top(matrix_input, row, column):
    # viewable distance upwards
    length = 1

    for i in range(len(matrix_input[:row:, column])):
        # print(matrix_input[:row:, column][-1 - i])
        if matrix_input[:row:, column][-1 - i] < matrix_input[row][column] \
                and i != (len(matrix_input[:row:, column]) - 1):
            length += 1
        else:
            break

    return length


def view_bottom(matrix_input, row, column):
    length = 1

    # print(matrix_input[row + 1:, column])

    for i in range(1, len(matrix_input[row + 1:, column])):
        # print(matrix_input[row + 1:, column][i])
        if matrix_input[row + 1:, column][i] < matrix_input[row][column]:
            length += 1
        else:
            break

    return length


def view_bottom(matrix_input, row, column):
    length = 1

    # print(matrix_input[row + 1:, column])

    for i in range(len(matrix_input[row + 1:, column]) - 1):
        # print(matrix_input[row + 1:, column][i])
        if matrix_input[row + 1:, column][i] < matrix_input[row][column]:
            length += 1
        else:
            break

    return length


def view_left(matrix_input, row, column):
    # viewable distance left
    length = 1

    # print(matrix_input[row][:column])

    for i in range(len(matrix_input[row][:column]) - 1):
        # print(matrix_input[row][:column][-i - 1])
        if matrix_input[row][:column][-i - 1] < matrix_input[row][column]:
            length += 1
        else:
            break

    return length


def view_right(matrix_input, row, column):
    # viewable distance right
    length = 1

    # print(matrix_input[row][column + 1:])

    for i in range(len(matrix_input[row][column + 1:]) - 1):
        # print(matrix_input[row][column + 1:][i])
        if matrix_input[row][column + 1:][i] < matrix_input[row][column]:
            length += 1
        else:
            break

    return length


def two(matrix_input):
    largest_mult = 0

    for i in range(1, len(matrix_input) - 1):
        for j in range(1, len(matrix_input[i]) -1 ):
            '''
            print(matrix_input[i][j])
            print("top " + str(view_top(matrix_input, i, j)))
            print("left " + str(view_left(matrix_input, i, j)))
            print("bottom " + str(view_bottom(matrix_input, i, j)))
            print("right " + str(view_right(matrix_input, i, j)))
            print("res " + str((view_top(matrix_input, i, j) * view_bottom(matrix_input, i, j) *
                           view_left(matrix_input, i, j) * view_right(matrix_input, i, j))))
            '''

            if (view_top(matrix_input, i, j) * view_bottom(matrix_input, i, j) *
                view_left(matrix_input, i, j) * view_right(matrix_input, i, j)) > largest_mult:
                largest_mult = (view_top(matrix_input, i, j) * view_bottom(matrix_input, i, j) *
                           view_left(matrix_input, i, j) * view_right(matrix_input, i, j))

    return largest_mult


file = open('input.txt', 'r')
# print(one(load_file(file)))
print(two(load_file(file)))
