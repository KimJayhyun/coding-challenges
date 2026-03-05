# https://school.programmers.co.kr/learn/courses/30/lessons/86491


def solution(sizes):
    max_w = max(max(w, h) for w, h in sizes)  # max(generator)
    max_h = max(min(w, h) for w, h in sizes)

    return max_w * max_h


# def solution(sizes):
#     max_w = -1
#     max_h = -1
#     for size in sizes:
#         if size[0] >= size[1]:
#             max_w = max(max_w, size[0])
#             max_h = max(max_h, size[1])
#         else:
#             max_w = max(max_w, size[1])
#             max_h = max(max_h, size[0])

#     return max_w * max_h


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))  # 	4000
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))  # 120
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))  # 133
