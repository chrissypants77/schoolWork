"""
    C.Marriott
    28/02/2025
    Dateiname: structtest.py
    Kommentar: Magische Quadrate
"""

# === VARIABLES ===
matrix_size = 1
matrix = [[0]* matrix_size for _ in range(matrix_size)]
cursor = [0, int(len(matrix[0])/2)]
current_number = 1

debug = False


# === FUNCTION ===
def matrix_debug(matrix_: list, curs: list, cn: int):
    print("Current matrix")
    print_matrix(matrix_)
    print("Cursor cursor: ", curs)
    print("Current number: ", cn)
    input("Enter for next step:")


def check_matrix(matrix_: list):
    count = 0
    for matrix_item in matrix_:
        if 0 not in matrix_item:
            count += 1

    if count == len(matrix_):
        return True
    return False


def print_matrix(matrix_: list):
    for row in matrix_:
        print(row)


# === MAIN PROGRAM ===
matrix[cursor[0]][cursor[1]] = current_number
current_number += 1


while not check_matrix(matrix):
    if debug:
        matrix_debug(matrix, cursor, current_number-1)

    if cursor[0] == 0:
        if cursor == [0, len(matrix[0])-1]:
            cursor[0] += 1
        else:
            cursor[1] += 1
            cursor[0] = len(matrix)-1
    else:
        if cursor[1] == len(matrix[0])-1:
            cursor[0] -= 1
            cursor[1] = 0
        else:
            cursor[0] -= 1
            cursor[1] += 1
            if matrix[cursor[0]][cursor[1]] != 0:
                cursor[0] += 2
                cursor[1] -= 1

    matrix[cursor[0]][cursor[1]] = current_number
    current_number += 1

print_matrix(matrix)