def main():
    import sys

    length = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split(" ")))

    arr.sort()

    left = 0
    right = len(arr) - 1
    summation = 0
    closet_distance = float("inf")
    closet_idx = [left, right]

    while left < right:
        summation = arr[left] + arr[right]

        if summation == 0:
            print(f"{arr[left]} {arr[right]}")

        elif closet_distance > abs(summation):
            closet_distance = abs(summation)
            closet_idx = [left, right]

        if summation > 0:
            right -= 1
        else:
            left += 1

    print(f"{arr[closet_idx[0]]} {arr[closet_idx[1]]}")


if __name__ == "__main__":
    main()
