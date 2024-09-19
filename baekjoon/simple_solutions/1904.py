def get_inputs():
    import sys

    input_data = sys.stdin.read()

    return int(input_data)


def solution():
    given_number = get_inputs()

    if given_number == 1:
        return 1
    elif given_number == 2:
        return 2
    elif given_number == 3:
        return 3

    count_list = [1, 2, 3]

    for i in range(3, given_number):
        result = (count_list[i - 1] + count_list[i - 2]) % 15746

        count_list.append(result)

    return count_list[given_number - 1]


def main():
    print(solution())


if __name__ == "__main__":
    main()
