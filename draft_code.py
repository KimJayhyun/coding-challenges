def get_inputs():
    import sys

    input_data = sys.stdin.read()
    inputs = input_data.splitlines()

    return inputs


def solution(n):
    if n == 1:
        return 1

    target_num = 1

    digit = 1
    while True:
        digit += 1
        target_num = target_num * 10 + 1
        if target_num % n == 0:
            break

    return digit


def main():
    inputs = get_inputs()

    result = [solution(int(n)) for n in inputs]

    print(*result, sep="\n", end="")


if __name__ == "__main__":
    main()
