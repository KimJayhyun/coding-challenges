def get_inputs():
    import sys

    input_data = sys.stdin.read()
    inputs = input_data.splitlines()

    str_to_int_arr = lambda x: list(map(int, x.split()))

    node_count, edge_count, start_node = map(int, inputs[0].split())
    data = list(map(str_to_int_arr, inputs[1:]))

    return node_count, edge_count, start_node, data


def solution():
    node_count, edge_count, start_node, data = get_inputs()

    dfs = []
    bfs = []

    current_node = start_node

    for idx in range(edge_count):
        next_node = 0

        if current_node in data[idx]:
            pass


def main():
    print(solution())


if __name__ == "__main__":
    main()
