from collections import defaultdict

def getBoxIdx(row: int, col: int):
    row = row // 3
    col = col // 3

    return row * 3 + col

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowBits = [0] * 9
        colBits = [0] * 9
        boxBits = [0] * 9

        for row in range(9):
            for col in range(9):

                value = board[row][col]

                if (value == '.'):
                    continue

                bit = 1 << int(value)
                
                if rowBits[row] | bit == rowBits[row]:
                    return False
                if colBits[col] | bit == colBits[col]:
                    return False
                boxIdx = getBoxIdx(row, col);
                if boxBits[boxIdx] | bit == boxBits[boxIdx]:
                    return False

                rowBits[row] |= bit
                colBits[col] |= bit
                boxBits[boxIdx] |= bit

        return True
