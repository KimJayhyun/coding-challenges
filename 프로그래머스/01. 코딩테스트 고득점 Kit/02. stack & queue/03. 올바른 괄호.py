# https://school.programmers.co.kr/learn/courses/30/lessons/12909


def solution(s):
    stack = []

    for char in s:
        if ")" == char:
            if len(stack) == 0:
                return False

            if "(" == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return len(stack) == 0


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
