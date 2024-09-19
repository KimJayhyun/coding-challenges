def get_inputs():
    import sys

    input_data = sys.stdin.read()
    inputs = input_data.splitlines()

    return int(inputs[0]), list(map(int, inputs[1:]))


def solution(n):
    count_list = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

    for i in range(10, n):
        count_list.append(count_list[i - 1] + count_list[i - 5])

    return count_list[n - 1]


def main():
    _, inputs = get_inputs()

    result = [solution(n) for n in inputs]

    print(*result, sep="\n", end="")


if __name__ == "__main__":
    main()
