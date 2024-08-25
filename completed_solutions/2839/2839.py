def get_inputs():
    import sys

    input_data = sys.stdin.read()
    return int(input_data)


def solution():
    max_weight = get_inputs()

    if max_weight == 3:
        return 1
    elif max_weight == 5:
        return 1

    count_table = [0, -1, -1, 1, -1, 1]

    for i in range(6, max_weight + 1):
        if count_table[i - 3] == -1 and count_table[i - 5] == -1:
            count_table.append(-1)
        elif count_table[i - 3] == -1:
            count_table.append(count_table[i - 5] + 1)
        elif count_table[i - 5] == -1:
            count_table.append(count_table[i - 3] + 1)
        else:
            count_table.append(min(count_table[i - 3] + 1, count_table[i - 5] + 1))

    return count_table[max_weight]


def main():
    print(solution())


if __name__ == "__main__":
    main()
