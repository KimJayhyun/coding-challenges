# https://school.programmers.co.kr/learn/courses/30/lessons/42840


def solution(answers):
    from itertools import cycle

    counts = [0, 0, 0]

    way_1 = cycle([1, 2, 3, 4, 5])
    way_2 = cycle([2, 1, 2, 3, 2, 4, 2, 5])
    way_3 = cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])

    for answer in answers:
        answer_1 = next(way_1)
        answer_2 = next(way_2)
        answer_3 = next(way_3)

        if answer == answer_1:
            counts[0] += 1
        if answer == answer_2:
            counts[1] += 1
        if answer == answer_3:
            counts[2] += 1

    max_count = max(counts)
    result = [index + 1 for index, count in enumerate(counts) if count == max_count]

    return result


print(solution([1, 2, 3, 4, 5]))  # 	[1]
print(solution([1, 3, 2, 4, 2]))  # 	[1,2,3]
