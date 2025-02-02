def get_inputs():
    import sys

    input_data = sys.stdin.read()
    inputs = input_data.splitlines()

    item_count = int(inputs[0])
    data = list(map(int, inputs[1:]))

    return item_count, data


def find_index_with_binary_search(arr, target):
    if not arr:
        return 0

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return left


def main():
    _, data = get_inputs()

    arr = []

    for idx, item in enumerate(data):
        insert_pos = find_index_with_binary_search(arr, item)

        arr.insert(insert_pos, item)

        left_mid_index = int(idx // 2)
        print(arr[left_mid_index])


if __name__ == "__main__":
    main()
