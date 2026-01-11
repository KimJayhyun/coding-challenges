"""
udemy.Python Data Structures & Algorithms.05. Hash Tables.01_1.common_problem의 Docstring

두 리스트에 같은 Item이 있는지 확인
    1. for loop: O(n^2)
    2. hash tables: O(n)
"""

list1 = [1, 3, 5]
list2 = [2, 4, 5]


def common1(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True

    return False


def common2(list1, list2):
    hash_table = {}

    # O(1 * n)
    for i in list1:
        hash_table[i] = True

    # O(1 * n)
    for j in list2:
        if j in hash_table:
            return True

    return False


print(f"common1: {common1(list1, list2)}")
print(f"common2: {common2(list1, list2)}")
