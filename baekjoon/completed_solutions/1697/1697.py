def get_inputs():
    import sys

    input_data = sys.stdin.read()
    n, m = map(int, input_data.split())

    return n, m


def solution():
    from collections import defaultdict

    n, m = get_inputs()

    max_value = 100000

    bfs = defaultdict(int)
    visited = [0] * (max_value + 1)
    need_visited = [n]

    while need_visited:
        now = need_visited.pop(0)

        if now == m:
            return bfs[now]

        for next_node in [now - 1, now + 1, now * 2]:
            if 0 <= next_node <= 100000 and not visited[next_node]:
                need_visited.append(next_node)

                visited[next_node] = 1
                bfs[next_node] = bfs[now] + 1

    return bfs[m]


def main():
    print(solution(), end="")


if __name__ == "__main__":
    main()
