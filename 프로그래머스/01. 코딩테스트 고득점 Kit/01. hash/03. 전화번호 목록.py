# https://school.programmers.co.kr/learn/courses/30/lessons/42577?language=python3


def solution(phone_book):
    phone_set = set()

    for phone in phone_book:
        phone_set.add(phone)

    for phone in phone_set:
        for i in range(len(phone)):
            if phone[:i] in phone_set:
                return False

    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
