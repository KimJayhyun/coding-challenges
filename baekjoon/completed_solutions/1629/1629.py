def solution(x, y, n):
    if x == 1:
        return 1

    if y == 1:
        return x % n

    root_x = solution(x, y // 2, n)

    if y % 2 == 0:
        return (root_x * root_x) % n
    else:
        return (root_x * root_x * x) % n


def main():
    import sys

    input_line = sys.stdin.readline()

    x, y, n = map(int, input_line.split(" "))

    answer = solution(x, y, n)

    print(answer)


if __name__ == "__main__":
    main()
