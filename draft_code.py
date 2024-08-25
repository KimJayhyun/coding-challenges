def get_inputs():
    import sys

    input_data = sys.stdin.read()
<<<<<<< HEAD

=======
>>>>>>> 2839
    return int(input_data)


def solution():
<<<<<<< HEAD
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
=======
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
>>>>>>> 2839


def main():
    print(solution())


if __name__ == "__main__":
    main()
