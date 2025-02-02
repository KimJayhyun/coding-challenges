def solution():
    import heapq
    import sys

    number_of_item = int(sys.stdin.readline())

    left_max_heap = []
    right_min_heap = []

    for _ in range(number_of_item):
        item = int(sys.stdin.readline())

        if len(left_max_heap) == len(right_min_heap):
            heapq.heappush(left_max_heap, -item)
        else:
            heapq.heappush(right_min_heap, item)

        if right_min_heap and right_min_heap[0] < -left_max_heap[0]:
            right = heapq.heappop(right_min_heap)
            left = heapq.heappop(left_max_heap)

            heapq.heappush(left_max_heap, -right)
            heapq.heappush(right_min_heap, -left)

        # print(f"answer: {-left_max_heap[0]}")
        print(-left_max_heap[0])


def main():
    solution()


if __name__ == "__main__":
    main()
