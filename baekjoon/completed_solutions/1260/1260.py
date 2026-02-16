def get_inputs():
    import sys

    input_data = sys.stdin.read()
    inputs = input_data.splitlines()

    node_count, edge_count, start = map(int, inputs[0].split())

    str_to_int_arr = lambda x: list(map(int, x.split()))

    data = list(map(str_to_int_arr, inputs[1:]))

    return node_count, edge_count, start, data


def solution():
    from collections import defaultdict

    node_count, _, start, data = get_inputs()

    ## 인접 리스트 생성
    adjacency_list = defaultdict(list)

    for edge in data:
        adjacency_list[edge[0]].append(edge[1])
        adjacency_list[edge[1]].append(edge[0])

    ## 인접 리스트 정렬
    for key in adjacency_list.keys():
        adjacency_list[key].sort()

    ## dfs : Stack
    def dfs(start):
        dfs = []
        visited = [False] * (node_count + 1)
        need_visited = [start]

        while need_visited:
            node = need_visited.pop()

            if not visited[node]:
                dfs.append(node)
                visited[node] = True

                for next_node in adjacency_list[node][::-1]:
                    need_visited.append(next_node)

        return dfs

    ## bfs : Queue
    def bfs(start):
        bfs = []
        visited = [False] * (node_count + 1)
        need_visited = [start]

        while need_visited:
            node = need_visited.pop(0)

            if not visited[node]:
                bfs.append(node)
                visited[node] = True

                for next_node in adjacency_list[node]:
                    need_visited.append(next_node)

        return bfs

    print(" ".join(map(str, dfs(start))))
    print(" ".join(map(str, bfs(start))))


def main():
    solution()


if __name__ == "__main__":
    main()
