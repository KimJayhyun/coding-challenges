def get_inputs():
    import sys

    input_data = sys.stdin.read()
    inputs = input_data.splitlines()

    item_count = int(inputs[0])

    string_to_int_arr = lambda x: list(map(int, x.split()))
    data = list(map(string_to_int_arr, inputs[1:]))

    return item_count, data


def solution(data):
    """
    이 함수는 좌표 6개의 리스트를 입력으로 받습니다:
    - (x1, y1, d1, x2, y2, d2)

    함수는 두 원의 관계를 나타내는 정수를 반환합니다:
    - -1: 두 원이 동일 (중심과 반지름이 동일함).
    - 0: 두 원이 서로 교차하지 않거나 떨어져 있음.
    - 1: 두 원이 외부 또는 내부에서 접함.
    - 2: 두 원이 두 점에서 교차함.

    Args:
        data (list): 6개의 숫자를 포함하는 리스트 [x1, y1, d1, x2, y2, d2]

    Returns:
        int: 두 원의 관계를 나타내는 정수.

    예제:
        >>> solution([0, 0, 5, 8, 0, 5])
        2

        >>> solution([0, 0, 5, 8, 0, 3])
        1

        >>> solution([0, 0, 5, 0, 0, 5])
        -1
    """
    x1, y1, d1, x2, y2, d2 = data

    if x1 == x2 and y1 == y2:
        if d1 == d2:
            return -1
        else:
            return 0

    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    max_d = max(d1, d2, distance)

    remaining_sum = d1 + d2 + distance - max_d

    if remaining_sum > max_d:
        return 2
    elif remaining_sum < max_d:
        return 0
    else:
        return 1


def main():
    _, data = get_inputs()

    result = [solution(d) for d in data]

    print(*result, sep="\n", end="")


if __name__ == "__main__":
    main()
