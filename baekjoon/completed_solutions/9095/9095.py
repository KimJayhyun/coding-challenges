def get_inputs():
    import sys

    input_data = sys.stdin.read()
    inputs = input_data.splitlines()

    return int(inputs[0]), list(map(int, inputs[1:]))


def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    count_table = [0, 1, 2, 4]

    for idx in range(4, n + 1):
        count_table.append(
            count_table[idx - 1] + count_table[idx - 2] + count_table[idx - 3]
        )

    return count_table[-1]


def main():
    _, inputs = get_inputs()

    result = [solution(n) for n in inputs]

    print(*result, sep="\n", end="")


if __name__ == "__main__":
    main()
