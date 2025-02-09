"""
C[i][j] = sum(A[i][k] * B[k][j]) for k = 0 to n-1
"""

import unittest


def matrix_multiplication(A, B):
    cols_A = len(A[0])
    rows_B = len(B)
    if not cols_A == rows_B:
        raise IndexError

    rows_A = len(A)
    cols_B = len(B[0])

    # rows_A 행 // cols_B 열
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


class TestMatrixMultiplication(unittest.TestCase):

    def test_multiplication_2x2(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        expected_result = [[19, 22], [43, 50]]
        result = matrix_multiplication(A, B)
        self.assertEqual(result, expected_result)

    def test_multiplication_3x3(self):
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        expected_result = [[30, 24, 18], [84, 69, 54], [138, 114, 90]]
        result = matrix_multiplication(A, B)
        self.assertEqual(result, expected_result)

    def test_multiplication_2x3_with_3x2(self):
        A = [[1, 2, 3], [4, 5, 6]]
        B = [[7, 8], [9, 10], [11, 12]]
        expected_result = [[58, 64], [139, 154]]
        result = matrix_multiplication(A, B)
        self.assertEqual(result, expected_result)

    def test_multiplication_identity_matrix(self):
        A = [[1, 2], [3, 4]]
        B = [[1, 0], [0, 1]]  # Identity matrix
        expected_result = [[1, 2], [3, 4]]
        result = matrix_multiplication(A, B)
        self.assertEqual(result, expected_result)

    def test_multiplication_zero_matrix(self):
        A = [[1, 2], [3, 4]]
        B = [[0, 0], [0, 0]]
        expected_result = [[0, 0], [0, 0]]
        result = matrix_multiplication(A, B)
        self.assertEqual(result, expected_result)

    def test_invalid_dimensions(self):
        A = [[1, 2]]
        B = [[1], [2], [3]]
        with self.assertRaises(IndexError):
            matrix_multiplication(A, B)


if __name__ == "__main__":
    unittest.main()
