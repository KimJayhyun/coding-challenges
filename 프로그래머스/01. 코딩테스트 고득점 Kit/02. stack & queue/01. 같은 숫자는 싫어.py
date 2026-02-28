# https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3


def solution(arr):
    result = [arr[0]]

    for number in arr[1:]:
        if number != result[-1]:
            result.append(number)

    return result


print(solution([1, 1, 3, 3, 0, 1, 1]))  # [1, 3, 0, 1]
print(solution([4, 4, 4, 3, 3]))  # [4, 3]
