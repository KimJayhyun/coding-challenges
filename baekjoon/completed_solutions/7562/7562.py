def get_inputs():
    import sys

    input_data = sys.stdin.read()
    inputs = input_data.splitlines()

    input_count = int(inputs[0])
    data = []

    for i in range(input_count):
        size = int(inputs[3 * i + 1])
        start_point = list(map(int, inputs[3 * i + 2].split()))
        end_point = list(map(int, inputs[3 * i + 3].split()))

        data.append([size, start_point, end_point])

    return input_count, data


def solution(size, start_point, end_point):
    visited = [[0] * size for _ in range(size)]
    need_visited = [start_point]

    while need_visited:
        now_x, now_y = need_visited.pop(0)

        if [now_x, now_y] == end_point:
            return visited[now_x][now_y]

        for x_step, y_step in [
            (x, y) for x in (-2, -1, 1, 2) for y in (-2, -1, 1, 2) if abs(x) != abs(y)
        ]:
            next_x, next_y = now_x + x_step, now_y + y_step

            if (
                0 <= next_x < size
                and 0 <= next_y < size
                and visited[next_x][next_y] == 0
            ):
                need_visited.append([next_x, next_y])
                visited[next_x][next_y] = visited[now_x][now_y] + 1


def main():
    _, data = get_inputs()

    result = [
        solution(size, start_point, end_point)
        for (size, start_point, end_point) in data
    ]

    print(*result, sep="\n", end="")


if __name__ == "__main__":
    main()
