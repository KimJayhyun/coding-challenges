def get_inputs():
    import sys

    input_data = sys.stdin.read()
    inputs = input_data.splitlines()

    length = int(inputs[0])
    data = list(map(list, inputs[1:]))

    return length, data


def solution():
    from collections import defaultdict

    length, data = get_inputs()

    visited = [[0] * length for _ in range(length)]

    group_table = [[0] * length for _ in range(length)]
    group_count_list = []
    group_number = 0

    need_visited = []

    for current_row, current_col in [
        (row, col) for row in range(length) for col in range(length)
    ]:
        if data[current_row][current_col] == "0":
            continue

        if visited[current_row][current_col] == 1:
            continue

        group_number += 1
        group_count = 0
        need_visited.append((current_row, current_col))

        while need_visited:
            current_row, current_col = need_visited.pop(0)

            if visited[current_row][current_col] == 0:
                visited[current_row][current_col] = 1
                group_table[current_row][current_col] = group_number
                group_count += 1

                for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    next_row, next_col = current_row + d_row, current_col + d_col

                    if (
                        0 <= next_row < length
                        and 0 <= next_col < length
                        and visited[next_row][next_col] == 0
                        and data[next_row][next_col] == "1"
                    ):
                        need_visited.append((next_row, next_col))

        group_count_list.append(group_count)

    group_count_list.sort()

    print(len(group_count_list))
    print(*group_count_list, sep="\n", end="")


def main():
    solution()


if __name__ == "__main__":
    main()
