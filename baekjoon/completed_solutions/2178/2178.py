def get_inputs():
    import sys

    input_data = sys.stdin.read()
    inputs = input_data.splitlines()

    max_row, max_col = map(int, inputs[0].split())
    data = list(map(list, inputs[1:]))

    return max_row, max_col, data


def solution():
    max_row, max_col, data = get_inputs()

    dfs = [(0, 0)]
    visited = []

    count = 0

    while True:
        current_position = dfs.pop()
        visited.append(current_position)

        if current_position == (max_row - 1, max_col - 1):
            break
        current_row, current_col = current_position

        count += 1

        # 오른쪽으로 이동
        if current_col + 1 < max_col:
            if (
                data[current_row][current_col + 1] == "1"
                and (current_row, current_col + 1) not in visited
            ):
                dfs.append((current_row, current_col + 1))
                continue

        # 아래로 이동
        if current_row + 1 < max_row:
            if (
                data[current_row + 1][current_col] == "1"
                and (current_row + 1, current_col) not in visited
            ):
                dfs.append((current_row + 1, current_col))
                continue

        # 위로 이동
        if current_row - 1 >= 0:
            if (
                data[current_row - 1][current_col] == "1"
                and (current_row - 1, current_col) not in visited
            ):
                dfs.append((current_row - 1, current_col))
                continue

        # 왼쪽으로 이동
        if current_col - 1 >= 0:
            if (
                data[current_row][current_col - 1] == "1"
                and (current_row, current_col - 1) not in visited
            ):
                dfs.append((current_row, current_col - 1))
                continue

        visited.pop()

    return len(visited)


def main():
    print(solution())


if __name__ == "__main__":
    main()
