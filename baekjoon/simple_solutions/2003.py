def get_inputs():
    import sys

    input_data = sys.stdin.read()
    inputs = input_data.splitlines()

    item_count, target = map(int, inputs[0].split())
    data = list(map(int, inputs[1].split()))

    return item_count, target, data


def solution():
    """
    Two Pointer
    """
    _, target, data = get_inputs()

    count = 0

    for i in range(len(data)):
        total = data[i]

        # i 번째 값이 target인 경우
        if total == target:
            count += 1
        elif total > target:
            continue

        # 부분합이 target인 경우
        for j in range(i + 1, len(data)):
            total += data[j]

            if total == target:
                count += 1
            elif total > target:
                break

    return count


def main():
    print(solution(), end="")


if __name__ == "__main__":
    main()
