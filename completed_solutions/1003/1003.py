def get_inputs():
    import sys

    input_data = sys.stdin.read()
    inputs = input_data.splitlines()

    item_count = int(inputs[0])
    data = map(int, inputs[1:])

    return item_count, data


def solution(n):
    """
    [0이 호출되는 횟수, 1이 호출되는 횟수]
    """
    if n == 0:
        return "1 0"
    elif n == 1:
        return "0 1"

    result = [[1, 0], [0, 1]]

    for _ in range(2, n + 1):
        result.append([result[-1][0] + result[-2][0], result[-1][1] + result[-2][1]])

    return " ".join(map(str, result[-1]))


def main():
    _, inputs = get_inputs()

    result = [solution(n) for n in inputs]

    print(*result, sep="\n", end="")


if __name__ == "__main__":
    main()
