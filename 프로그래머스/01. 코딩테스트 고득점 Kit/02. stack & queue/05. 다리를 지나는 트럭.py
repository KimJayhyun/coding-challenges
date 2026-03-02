# https://school.programmers.co.kr/learn/courses/30/lessons/42583


def solution(bridge_length, weight, truck_weights):
    from collections import deque

    second_count = 0
    truck_weights_queue = deque(truck_weights)
    current_weight = 0
    current_weight_queue = deque([])

    while truck_weights_queue or current_weight_queue:
        second_count += 1

        while (
            current_weight_queue
            and second_count - current_weight_queue[0][1] == bridge_length
        ):
            truck_weight, _ = current_weight_queue.popleft()
            current_weight -= truck_weight

        if truck_weights_queue and current_weight + truck_weights_queue[0] <= weight:
            truck_weight = truck_weights_queue.popleft()

            current_weight += truck_weight
            current_weight_queue.append((truck_weight, second_count))

    return second_count


print(solution(2, 10, [7, 4, 5, 6]))  # 	8
print(solution(100, 100, [10]))  # 	101
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # 	110
