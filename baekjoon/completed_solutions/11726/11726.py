def get_inputs():
    import sys

    input_data = sys.stdin.read()
    return int(input_data)


def solution():
    n = get_inputs()

    count_list = []

    # 2 x 1
    count_list.append(1)

    # 2 x 2
    count_list.append(2)

    for i in range(2, n + 1):
        ## Time 40 ms
        # if i // 40 == 0:
        #     count_list.append(count_list[i - 1] % 10007 + count_list[i - 2] % 10007)
        # else:
        #     count_list.append(count_list[i - 1] + count_list[i - 2])

        ## Time 36ms
        count_list.append(count_list[i - 1] + count_list[i - 2])

    return count_list[n - 1] % 10007


def main():
    print(solution())


if __name__ == "__main__":
    main()
