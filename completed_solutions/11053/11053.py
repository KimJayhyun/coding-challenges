def get_inputs():
    import sys

    input_data = sys.stdin.read()
    inputs = input_data.splitlines()

    return int(inputs[0]), list(map(int, inputs[1].split()))


def solution():
    item_count, data = get_inputs()

    length_table = [1] * item_count

    for i in range(1, item_count):
        for j in range(i):
            if data[j] < data[i]:
                length_table[i] = max(length_table[i], length_table[j] + 1)

    return max(length_table)

def main():
    print(solution(), end="")


if __name__ == "__main__":
    main()
