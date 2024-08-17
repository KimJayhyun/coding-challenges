def get_inputs():
    import sys

    input_data = sys.stdin.read()
    inputs = input_data.splitlines()

    str_to_int_arr = lambda x: list(map(int, x.split()))

    item_count, max_weight = map(int, inputs[0].split())
    data = list(map(str_to_int_arr, inputs[1:]))

    return item_count, max_weight, data


def solution():
    item_count, max_weight, data = get_inputs()

    if item_count == 1:
        return data[0][1] if data[0][0] <= max_weight else 0

    value_table = [0] * (max_weight + 1)

    for i in range(item_count):
        weight, value = data[i]

        if weight > max_weight:
            continue

        for looping_weight in range(max_weight, 0, -1):
            if (
                looping_weight + weight <= max_weight
                and value_table[looping_weight] != 0
            ):
                value_table[looping_weight + weight] = max(
                    value_table[looping_weight + weight],
                    value_table[looping_weight] + value,
                )

        value_table[weight] = max(value_table[weight], value)

    return max(value_table)


def main():
    print(solution())


if __name__ == "__main__":
    main()
