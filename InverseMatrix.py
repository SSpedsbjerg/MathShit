import numpy as np
import copy as copy

def swap_rows(A, row1, row2):
    temp = copy.copy(A[row1])
    A[row1] = copy.copy(A[row2])
    A[row2] = copy.copy(temp)
    return A

def inverse(A):
    #Divide the row with the number on the index of the row and column
    #It might say divide by zero, but it never does that because the rows has been switched by the time it reaches this function,
    #is just because Python is a scripting language such a warning would come up
    def step1(currentRow, placeholder=np.array):
        A[currentRow] /= A[currentRow][currentRow]
        idMatrix[currentRow] /= placeholder[currentRow][currentRow]

    # subtract row with the index of the row and column multiplied by the row from step1
    def step2(currentRow, runs, placeHolder=np.array):
        A[currentRow] -= A[currentRow][runs] * A[runs]
        idMatrix[currentRow] -= placeHolder[currentRow][runs] * idMatrix[runs]

    # Create Identity Matrix
    nrOfColumns = len(A)
    nrOfRows = len(A[0])
    column = []
    for j in range(nrOfRows):
        row = []
        for i in range(nrOfColumns):
            if (i == j):
                row.append(1)
            else:
                row.append(0)
        column.append(row)
    idMatrix = np.array(column, dtype=np.float32)

    # if it doesn't start with 1, move it to somewhere else
    if (A[0][0] != 1):
        tempRow = A[0]
        runs = 0
        for i in range(nrOfColumns):
            if (A[i][0] != 0):
                runs = i
                break

        swap_rows(A, 0, runs)
        if (runs != 0):
            idMatrix = swap_rows(idMatrix, 0, runs)

    #Calculate the inverse
    i = 0
    while i != nrOfRows:

        placeHolderA = copy.copy(A)
        step1(i, placeHolderA)

        for row in range(nrOfRows):
            if row == i:
                continue
            else:
                step2(row, i, copy.copy(placeHolderA))
        i += 1
    return idMatrix.round(3) #Round up the numbers to the 3rd decimal point


def test():
    test = 3

    originalA = np.array
    for i in range(6):
        if test == 3:
            A = np.array([[0, 2, 0], [1, 4, 2], [4, 2, 0]], dtype=np.float32)
            originalA = copy.copy(A)
        elif test == 4:
            A = np.array([[0, 2, 0, 8], [1, 4, 2, -2], [4, 2, 0, -3], [2, -1, -6, 5]], dtype=np.float32)
            originalA = copy.copy(A)
        elif test == 5:
            A = np.array([[0, 2, 0, 8, 1], [1, 2, 2, -2, 5], [4, 2, 0, -3, 2], [2, -1, -6, 5, 0], [-5, 3, 8, 4, 4]],
                         dtype=np.float32)
            originalA = copy.copy(A)
        else:
            A = np.random.rand(test, test)
            originalA = copy.copy(A)

        print("=== Test", test - 2, " ===\nStarted of with:\n",originalA.round(3), "\nInverse:\n", inverse(A), "\n")
        test += 1

if __name__ == "__main__":
    print('Running test')
    test()
