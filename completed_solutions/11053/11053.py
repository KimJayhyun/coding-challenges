def get_inputs():
    import sys

    input_data = sys.stdin.read()
    inputs = input_data.splitlines()

    return int(inputs[0]), list(map(int, inputs[1].split()))


def solution():
    item_count, data = get_inputs()

    if item_count == 1:
        return 1

    item_table = [0] + data
    length_table = [0] * (item_count + 1)

    for idx, item in enumerate(data):
        length = idx + 1

        max_temp = 0
        for i in range(length - 1, -1, -1):
            if item_table[i] >= item:
                continue
            else:
                max_temp = max(max_temp, length_table[i] + 1)

            length_table[length] = max_temp

    return max(length_table)


def main():
    print(solution(), end="")


if __name__ == "__main__":
    main()
