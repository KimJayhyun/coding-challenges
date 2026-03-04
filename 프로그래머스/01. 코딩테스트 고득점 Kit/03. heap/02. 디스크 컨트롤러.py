# https://school.programmers.co.kr/learn/courses/30/lessons/42627


def solution(jobs: list):
    import heapq
    from collections import deque

    jobs.sort(key=lambda x: x[0])

    summation = 0
    jobs_count = len(jobs)

    jobs_queue = deque(enumerate(jobs))
    stay_heap = []

    current_time = -1
    current_job = None
    while True:
        current_time += 1

        # 작업이 진행 중
        if current_job is not None:
            running_time, request_time, index, started_time = current_job

            # 작업 종료 확인
            if current_time - started_time == running_time:
                print(f"index: {index}")
                print(f"current_time: {current_time}")
                print(f"current_job: {current_job}")
                print("===")
                summation += current_time - request_time
                current_job = None

        # 요청 작업 대기 큐에 넣음
        while jobs_queue:
            index, (request_time, running_time) = jobs_queue[0]
            if current_time >= request_time:
                index, (request_time, running_time) = jobs_queue.popleft()

                # 1. 소요시간이 짧은 것
                # 2. 요청 시간이 빠른 것(작은 것)
                # 3. 작업 번호가 작은 것
                heapq.heappush(stay_heap, (running_time, request_time, index))
            else:
                break

        if current_job is None:
            if stay_heap:
                running_time, request_time, index = heapq.heappop(stay_heap)
                current_job = running_time, request_time, index, current_time
            elif jobs_queue:
                _, (next_request_time, _) = jobs_queue[0]
                current_time = next_request_time - 1

        if not stay_heap and not jobs_queue and current_job is None:
            break

    return summation // jobs_count


print(solution([[0, 3], [1, 9], [3, 5]]))  # 8

print(solution([[7, 8], [3, 5], [9, 6]]))  # 9
