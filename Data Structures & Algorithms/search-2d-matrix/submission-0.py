class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix) # rows
        n = len(matrix[0]) # cols

        def findRow() -> int:
            i = 0
            j = m - 1

            while i != j:

                mid = (i + j) // 2

                if matrix[i][0] <= target <= matrix[mid][n - 1]:
                    j = mid
                elif matrix[mid + 1][0] <= target <= matrix[j][n - 1]:
                    i = mid + 1
                else:
                    return -1

            return i

        row = findRow()

        if row == -1:
            return False

        i = 0
        j = n - 1

        while i != j:

            mid = (i + j) // 2

            if matrix[row][i] <= target <= matrix[row][mid]:
                j = mid
            elif matrix[row][mid + 1] <= target <= matrix[row][j]:
                i = mid + 1
            else:
                return False

        return matrix[row][i] == target