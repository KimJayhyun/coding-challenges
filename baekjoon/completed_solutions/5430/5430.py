def get_inputs():
    import sys

    input_data = sys.stdin.read()

    input_lines = input_data.splitlines()

    inputs = []
    for i in range(1, len(input_lines), 3):
        inputs.append(
            [
                # functions
                input_lines[i],
                # number of data
                int(input_lines[i + 1]),
                # data array
                (
                    []
                    if input_lines[i + 2] == "[]"
                    else list(map(int, input_lines[i + 2][1:-1].split(",")))
                ),
            ]
        )

    return inputs


def solution(n: list[str, int, list]):
    """
    Args:
        - n[0] (str): 'R'(뒤집기)과 'D'(삭제) 명령어로 구성된 문자열
        - n[1] (int): 데이터 배열의 길이
        - n[2] (list): 정수로 구성된 데이터 배열

    Returns:
        - 정상 실행 시: "[1,2,3]" 형태의 문자열
        - 에러 발생 시: "error" 문자열

    Examples:
        >>> solution(["RD", 4, [1,2,3,4]])
        "[4,3,2]"
        >>> solution(["D", 1, [42]])
        "[]"
        >>> solution(["D", 0, []])
        "error"
    """

    func = n[0]
    length_of_data = n[1]
    data = n[2]

    is_reverse = False
    for f in func:
        if f == "R":
            is_reverse = not is_reverse
        else:
            if not data:
                return "error"

            if is_reverse:
                data.pop()
            else:
                data.pop(0)

    if is_reverse:
        data.reverse()

    return "[" + ",".join(map(str, data)) + "]"


def main():
    inputs = get_inputs()

    result = [solution(n) for n in inputs]

    print(*result, sep="\n", end="")


if __name__ == "__main__":
    main()
