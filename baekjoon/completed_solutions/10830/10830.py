def get_inputs():
    import sys

    read_lines = sys.stdin.readline

    n, k = map(int, read_lines().split(" "))

    matrix = [[*map(int, read_lines().split(" "))] for _ in range(n)]

    return matrix, k


def solution(matrix, k, n):
    if k == 1:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = matrix[i][j] % 1000
        return matrix

    half = solution(matrix, k // 2, n)

    if k % 2 == 0:
        return multiplication(half, half, n)
    else:
        return multiplication(multiplication(half, half, n), matrix, n)


def multiplication(A, B, n):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] = (result[i][j] + (A[i][k] * B[k][j])) % n
    return result


def main():
    DIVISOR = 1000
    matrix, k = get_inputs()

    result = solution(matrix, k, DIVISOR)

    for row in result:
        print(*row)


if __name__ == "__main__":
    main()
