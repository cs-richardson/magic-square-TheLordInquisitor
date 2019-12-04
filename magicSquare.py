"""
This program prompt the user for and create magic squares. Function templates courtesy of Ms. Richardson's
 magicSquareStarter.py
---Program written by Son Nguyen---
"""

def fillSquare(n, sqArr):
    """
    This procedure prompts the user for n^2 inputs to populate a 2D square array which has already been declared
    Precondition:  sqArr has been declared with a size of nxn
    Function courtesy of Ms. Richardson
    """
    for r in range(n):
        print("----ROW " + str(r + 1) + "----")
        for c in range(n):
            sqArr[r][c] = int(input("Enter value: "))


def printSquare(n, sqArr):
    """
    This procedure prints a 2D square array of size n
    Function courtesy of Ms. Richardson
    """
    for r in range(n):
        for c in range(n):
            print(sqArr[r][c], end="\t")
        print("\n")


def checkRow(n, sqArr, mNum):
    """
    This procedure will return true if every row of sqArr has a sum of mNum
    """
    rowSum = 0
    for row in range(n):
        for col in range(n):
            rowSum = rowSum + sqArr[row][col]
        if rowSum != mNum:
            return False
        rowSum = 0
    return True


def checkCol(n, sqArr, mNum):
    """
    This procedure will return true if every column of sqArr has a sum of mNum
    """
    colSum = 0
    for row in range(n):
        for col in range(n):
            colSum = colSum + sqArr[col][row]
        if colSum != mNum:
            return False
        colSum = 0
    return True


def checkDiag1(n, sqArr, mNum):
    """
    This procedure will return true if the diagonal has a sum of mNum
    """
    diagSum = 0
    for row in range(n):
        diagSum = diagSum + sqArr[row][row]
    if diagSum != mNum:
        return False
    return True


def checkDiag2(n, sqArr, mNum):
    """
    This procedure will return true if the other diagonal  has a sum of mNum
    """
    diagSum = 0
    for row in range(n):
        diagSum = diagSum + sqArr[n - 1 - row][n - 1 - row]
    if diagSum != mNum:
        return False
    return True


def checkUnique(n, sqArr):
    """
    This procedure will return true if there are no repeating numbers
    """
    arr = []
    for row in range(n):
        for col in range(n):
            if sqArr[row][col] in arr:
                return False
            arr.append(sqArr[row][col])
    return True


def checkSquare(s, sqArr):
    """
    Returns True if inputed square is magic, and False if not.
    """
    mNum = s * ((s ** 2 + 1) / 2)
    if (checkRow(s, sqArr, mNum) and
            checkCol(s, sqArr, mNum) and
            checkDiag1(s, sqArr, mNum) and
            checkDiag2(s, sqArr, mNum) and
            checkUnique(s, sqArr)):
        return True
    else:
        return False


def doEverything():
    """
    This procedure do everything.
    """
    s = int(input("Enter square side length:  "))
    sq = [[0 for x in range(s)] for y in range(s)]
    # s = 3
    # sq = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    # sq = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    fillSquare(s, sq)
    printSquare(s, sq)
    print(checkSquare(s, sq))


doEverything()
