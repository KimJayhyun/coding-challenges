def get_inputs():
    import sys

    input_data = sys.stdin.read()
    inputs = input_data.splitlines()

    max_row, max_col = map(int, inputs[0].split())
    data = list(map(list, inputs[1:]))

    return max_row, max_col, data


def solution():
    max_row, max_col, data = get_inputs()

    visited = [[0] * (max_col) for _ in range(max_row)]
    count_table = [[1] * (max_col) for _ in range(max_row)]

    need_visited = [(0, 0)]

    while need_visited:
        current_row, current_col = need_visited.pop(0)

        if current_row == max_row - 1 and current_col == max_col - 1:
            break

        if visited[current_row][current_col] == 0:
            visited[current_row][current_col] = 1

            for row, col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_row = current_row + row
                next_col = current_col + col

                if (
                    0 <= next_row < max_row
                    and 0 <= next_col < max_col
                    and data[next_row][next_col] == "1"
                    and visited[next_row][next_col] == 0
                ):
                    need_visited.append((next_row, next_col))
                    count_table[next_row][next_col] = (
                        count_table[current_row][current_col] + 1
                    )

    return count_table[max_row - 1][max_col - 1]


def main():
    print(solution())


if __name__ == "__main__":
    main()
