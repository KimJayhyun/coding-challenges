def get_inputs():
    import sys

    input_data = sys.stdin.read()

    return int(input_data)


def solution():
    given_number = get_inputs()

    if given_number == 1:
        return 0
    elif given_number == 2:
        return 1

    count_table = [0, 0, 1]

    for number in range(3, given_number + 1):

        if number % 3 == 0 and number % 2 == 0:
            count_table.append(
                min(
                    count_table[number // 3] + 1,
                    count_table[number // 2] + 1,
                    count_table[number - 1] + 1,
                )
            )
        elif number % 3 == 0:
            count_table.append(
                min(count_table[number // 3] + 1, count_table[number - 1] + 1)
            )
        elif number % 2 == 0:
            count_table.append(
                min(count_table[number // 2] + 1, count_table[number - 1] + 1)
            )
        else:
            count_table.append(count_table[number - 1] + 1)

    return count_table[given_number]


def main():
    print(solution())


if __name__ == "__main__":
    main()
