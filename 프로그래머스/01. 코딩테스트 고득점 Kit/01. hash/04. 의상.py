# https://school.programmers.co.kr/learn/courses/30/lessons/42578


def solution(clothes):
    result = 1

    count_dict = {}
    for _, category in clothes:
        if category not in count_dict:
            count_dict[category] = 1
        else:
            count_dict[category] += 1

    for _, value in count_dict.items():
        result *= value + 1

    ## (아무것도 선택하지 않는 경우의 수) 1 + count 중 1 가지 선택
    ## 모든 category를 아무것도 선택하지 않는 경우 1 가지 제외
    # (n+1)_C_1 * ... * (n+1)_C_1 - 1
    return result - 1


print(
    solution(
        [
            ["yellow_hat", "headgear"],
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"],
        ]
    )
)
print(
    solution(
        [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    )
)
