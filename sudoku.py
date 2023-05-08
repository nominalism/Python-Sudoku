S = [['', '', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', '', '*']]

#Function to display the Sudoku board
def displaySudoku():
    print(' a b c d e f g h i')
    for row in range(9):
        print(chr(ord('A') + row) + ' ', end='')
        for col in range(9):
            print(S[row][col] + ' ', end='')
            if (col + 1) % 3 == 0:
                print(' ', end='')
        print()
        if (row + 1) % 3 == 0:
            print()

#Function to read user input for the cell value to update
def readCellValue():
    l, c, value = input("Row, Column, Value: ").split()
    row = ord(l) - ord('A')
    col = ord(c) - ord('a')
    if 0 <= row <= 8:
        if 0 <= col <= 8:
            if value == '*' or (ord('1') <= ord(value) <= ord('9')):
                return True, row, col
            else:
                print('Invalid value.')
                return False, 0, 0, ''
        else:
            print('Invalid column.')
            return False, 0, 0, ''
    else:
        print('Invalid row.')
        return False, 0, 0, ''

#Function to check if a value is valid for a row
def checkRow(S, row, col, value):
    for i in range(9):
        if i != col and S[row][i] == value:
            return False
    return True

#Function to check if a value is valid for a 3x3 quadrant
def checkQuadrant(S, row, col, value):
    row_quad = int(row / 3) * 3
    col_quad = int(col / 3) * 3
    for i in range(row_quad, row_quad + 3):
        for j in range(col_quad, col_quad + 3):
            if (i != row or j != col) and S[i][j] == value:
                return False
        return True

#Function to read the initial Sudoku board from user input
def readSudokuInstance():
    print(' Sudoku Instance: ')
    print(' a b c d e f g h i ')
    for i in range(9):
        message = chr(ord('A') + i )
        row = input(message + ' ').split()
        for k in range(9):
            S[i][k] = row[k]
    print()

readSudokuInstance()
displaySudoku()
inputValid = False

while not inputValid:
    inputValid, row, col, value = readCellValue()
    if inputValid:
        if checkRow(S, row, col, value) and checkQuadrant(S, row, col, value):
            S[row][col] = value
displaySudoku()
