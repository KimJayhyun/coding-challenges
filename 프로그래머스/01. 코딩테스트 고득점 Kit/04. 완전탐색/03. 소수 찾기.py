# https://school.programmers.co.kr/learn/courses/30/lessons/42839


def is_prime_number(number: int) -> bool:
    from math import sqrt

    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2

    for n in range(3, int(sqrt(number)) + 1, 2):
        if number % n == 0:
            return False

    return True


def solution(numbers):
    from itertools import permutations

    count = 0
    seen = set()

    for index in range(1, len(numbers) + 1):
        permutation_numbers = permutations(numbers, index)

        for number in permutation_numbers:
            number = int("".join(number))

            if number in seen:
                continue

            seen.add(number)

            if is_prime_number(number):
                count += 1

    return count


print(solution("17"))  # 3
print(solution("011"))  # 2
