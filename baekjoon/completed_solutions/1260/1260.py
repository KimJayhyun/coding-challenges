def get_inputs():
    import sys

    input_data = sys.stdin.read()
    inputs = input_data.splitlines()

    node_count, edge_count, start = inputs[0].split()
    data = list(map(lambda x: x.split(), inputs[1:]))

    return node_count, edge_count, start, data


def solution():
    from collections import defaultdict

    _, _, start, data = get_inputs()

    graph = defaultdict(list)

    for edge in data:
        graph[edge[0]].append(edge[1])

    for key in graph:
        graph[key].sort()

    def dfs(start):
        visited = []
        need_visited = [start]

        while need_visited:
            node = need_visited.pop()

            if node not in visited:
                visited.append(node)
                need_visited.extend(graph[node][::-1])

        return visited

    def bfs(start):
        visited = []
        need_visited = [start]

        while need_visited:
            node = need_visited.pop(0)

            if node not in visited:
                visited.append(node)
                need_visited.extend(graph[node])

        return visited

    print(" ".join(dfs(start)))
    print(" ".join(bfs(start)))


def main():
    solution()


if __name__ == "__main__":
    main()
