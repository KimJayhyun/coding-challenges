from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        ## 1. Make Transpose Matrix
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        ## 2. Reverse all rows
        for row in range(n):
            matrix[row] = matrix[row][::-1]

        return matrix


solution = Solution()
print(solution.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(solution.rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))
