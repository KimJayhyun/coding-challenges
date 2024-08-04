def get_inputs():
    import sys

    input_data = sys.stdin.read()
    inputs = map(int, input_data.splitlines())

    return inputs


def solution(n):
    """
    함수는 정수 n을 받아서 n의 배수인 1로만 구성된 가장 작은 숫자를 계산합니다.
    계산된 숫자의 자릿수를 반환합니다.
    """
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

    result = [solution(n) for n in inputs]

    print(*result, sep="\n", end="")


if __name__ == "__main__":
    main()
