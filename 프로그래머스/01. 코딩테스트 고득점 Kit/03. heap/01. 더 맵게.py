# https://school.programmers.co.kr/learn/courses/30/lessons/42626


def solution(scoville, K):
    import heapq

    heapq.heapify(scoville)

    count = 0
    while True:
        latest_value = heapq.heappop(scoville)

        if not scoville:
            if latest_value < K:
                return -1
            else:
                break
        elif latest_value < K:
            count += 1

            second_latest_value = heapq.heappop(scoville)
            heapq.heappush(scoville, latest_value + 2 * second_latest_value)
        else:
            break

    return count


print(solution([1, 2, 3, 9, 10, 12], 7))  # 2
