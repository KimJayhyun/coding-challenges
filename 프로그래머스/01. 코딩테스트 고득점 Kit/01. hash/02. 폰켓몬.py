# https://school.programmers.co.kr/learn/courses/30/lessons/1845


def solution(nums):
    max_size = len(nums) // 2
    set_numbers = set(nums)

    return min(len(set_numbers), max_size)
