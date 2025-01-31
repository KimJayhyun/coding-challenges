def get_inputs():
    import sys

    input_data = sys.stdin.read()
    inputs = input_data.splitlines()

    item_count = int(inputs[0])
    data = list(map(int, inputs[1].split(" ")))

    return item_count, data


def solution(item_count, data):
    data.sort()

    left, right = 0, item_count - 1

    closest_distance = float("inf")
    answer = None

    while left < right:
        sum = data[left] + data[right]

        if sum == 0:
            return str(data[left]) + " " + str(data[right])

        distance = abs(sum)

        if closest_distance > distance:
            answer = [data[left], data[right]]
            closest_distance = distance

        if sum > 0:
            right -= 1
        else:
            left += 1

    return str(answer[0]) + " " + str(answer[1])


def main():
    item_count, data = get_inputs()

    result = solution(item_count, data)
    print(result)


if __name__ == "__main__":
    main()
