def get_inputs():
    import sys

    input_data = sys.stdin.read()
    inputs = input_data.splitlines()

    return map(int, inputs)


def solution(n):
    pass


def main():
    inputs = get_inputs()

    result = [solution(n) for n in inputs]

    print(result, sep="\n", end="")


if __name__ == "__main__":
    main()
