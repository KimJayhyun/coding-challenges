# https://school.programmers.co.kr/learn/courses/30/lessons/42586


def solution(progresses, speeds):
    import math

    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]

    result = []
    index = 0
    while index < len(days):
        base = days[index]
        count = 0

        while index < len(days) - 1 and days[index + 1] <= base:
            index += 1
            count += 1

        index += 1

        result.append(count + 1)

    return result


# def solution(progresses, speeds):
#     result = []

#     while progresses:
#         release_count = 1

#         progress = progresses.pop(0)
#         speed = speeds.pop(0)

#         ratio = (100 - progress) // speed
#         if (100 - progress) % speed != 0:
#             ratio += 1

#         for index, speed in enumerate(speeds):
#             progresses[index] = progresses[index] + ratio * speed

#         while progresses:
#             progress = progresses[0]
#             if progress >= 100:
#                 progresses.pop(0)
#                 speeds.pop(0)

#                 release_count += 1
#                 continue

#             break

#         result.append(release_count)

#     return result


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
