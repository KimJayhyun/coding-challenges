# https://school.programmers.co.kr/learn/courses/30/lessons/42584


def solution(prices):
    stack = []
    answer = [0] * len(prices)

    for i in range(len(prices)):
        # 가격이 떨어지면 이전 것들 처리
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top

        stack.append(i)

    # 끝까지 안 떨어진 것들 처리
    while stack:
        top = stack.pop()
        answer[top] = len(prices) - 1 - top

    return answer


print(solution([1, 2, 3, 2, 3]))  # [4, 3, 1, 1, 0]
