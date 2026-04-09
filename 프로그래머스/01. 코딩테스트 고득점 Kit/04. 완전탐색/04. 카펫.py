# https://school.programmers.co.kr/learn/courses/30/lessons/42842


def solution(brown, yellow):
    total = brown + yellow

    for h in range(3, total + 1):
        if total % h != 0:
            continue
        w = total // h
        if w < h:
            break
        if 2 * w + 2 * h - 4 == brown and (w - 2) * (h - 2) == yellow:
            return [w, h]


print(solution(10, 2))   # [4, 3]
print(solution(24, 24))  # [8, 6]
print(solution(8, 1))    # [3, 3]
