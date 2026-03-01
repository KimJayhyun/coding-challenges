# https://school.programmers.co.kr/learn/courses/30/lessons/42587?language=python3


def solution(priorities, location):
    import heapq
    from collections import deque

    # max 값
    priorities_heap = [-priority for priority in priorities]
    heapq.heapify(priorities_heap)

    location_list = [i for i in range(len(priorities))]

    priorities_queue = deque(priorities)
    location_queue = deque(location_list)

    result = 0
    is_max_priority = False
    max_priority = -1 * heapq.heappop(priorities_heap)
    while priorities_queue:
        process_priority = priorities_queue.popleft()
        process_location = location_queue.popleft()

        is_max_priority = process_priority == max_priority
        if not is_max_priority:
            priorities_queue.append(process_priority)
            location_queue.append(process_location)
        else:
            if priorities_heap:
                max_priority = -1 * heapq.heappop(priorities_heap)

            result += 1

            if location == process_location:
                break

    return result


print(solution([2, 1, 3, 2], 2))  # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5
