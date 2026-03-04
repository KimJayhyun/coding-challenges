# https://school.programmers.co.kr/learn/courses/30/lessons/42628


def solution(operations):
    import heapq

    deleted = set()
    minimum_heap = []
    maximum_heap = []
    uid = 0

    for operation in operations:
        if operation.startswith("I"):
            number = int(operation.split(" ")[1])
            heapq.heappush(minimum_heap, (number, uid))
            heapq.heappush(maximum_heap, (-number, uid))
            uid += 1

        elif "D -1" == operation:
            while minimum_heap and minimum_heap[0][1] in deleted:
                heapq.heappop(minimum_heap)

            if not minimum_heap:
                continue

            number, i = heapq.heappop(minimum_heap)
            deleted.add(i)

        elif "D 1" == operation:
            while maximum_heap and maximum_heap[0][1] in deleted:
                heapq.heappop(maximum_heap)

            if not maximum_heap:
                continue

            number, i = heapq.heappop(maximum_heap)
            deleted.add(i)

    while maximum_heap and maximum_heap[0][1] in deleted:
        heapq.heappop(maximum_heap)

    if not maximum_heap:
        return [0, 0]

    maximum = -maximum_heap[0][0]

    while minimum_heap and minimum_heap[0][1] in deleted:
        heapq.heappop(minimum_heap)

    if not minimum_heap:
        return [maximum, maximum]

    minimum = minimum_heap[0][0]
    return [maximum, minimum]


# def solution(operations):
#     import heapq

#     queue = []

#     for operation in operations:
#         if "I" in operation:
#             number = int(operation.split(" ")[1])

#             queue.append(number)

#         elif "D -1" == operation:
#             if not queue:
#                 continue

#             heapq.heapify(queue)
#             heapq.heappop(queue)

#         elif "D 1" == operation:
#             if not queue:
#                 continue

#             queue = [-x for x in queue]
#             heapq.heapify(queue)
#             heapq.heappop(queue)
#             queue = [-x for x in queue]

#     if not queue:
#         return [0, 0]

#     heapq.heapify(queue)
#     minimum = heapq.heappop(queue)

#     result = [minimum, minimum]

#     if not queue:
#         return result

#     queue = [-x for x in queue]
#     heapq.heapify(queue)
#     maximum = heapq.heappop(queue)

#     return [-maximum, minimum]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))  # [0,0]
print(
    solution(
        ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    )
)  # [333, -45]
