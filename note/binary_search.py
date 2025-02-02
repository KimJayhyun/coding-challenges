import unittest


def binary_search(arr, target):
    """정렬된 배열에서 이진 탐색을 수행하여 target 값의 인덱스를 반환합니다.

    Args:
        arr (list): 오름차순으로 정렬된 정수 배열
        target (int): 찾고자 하는 값

    Returns:
        int: target이 있는 인덱스. target이 배열에 없으면 -1을 반환

    Examples:
        >>> binary_search([1, 3, 5, 7, 9], 5)
        2
        >>> binary_search([1, 3, 5, 7, 9], 6)
        -1
        >>> binary_search([], 5)
        -1
        >>> binary_search([1, 3, 3, 3, 5], 3)
        2  # 중복된 값이 있는 경우 해당 값의 인덱스 중 하나를 반환
    """

    if not arr:
        return -1

    # 범위에 벗어나는 경우
    if arr[0] > target or arr[-1] < target:
        return -1

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


class TestBinarySearch(unittest.TestCase):
    def test_basic_cases(self):
        # 기본적인 케이스
        arr1 = [1, 3, 5, 7, 9, 11, 13, 15]
        self.assertEqual(binary_search(arr1, 7), 3)  # 중간 값 찾기
        self.assertEqual(binary_search(arr1, 1), 0)  # 첫 번째 원소 찾기
        self.assertEqual(binary_search(arr1, 15), 7)  # 마지막 원소 찾기

    def test_not_found(self):
        # 존재하지 않는 값 찾기
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(arr, 4), -1)  # 배열 중간의 없는 값
        self.assertEqual(binary_search(arr, 0), -1)  # 최솟값보다 작은 값
        self.assertEqual(binary_search(arr, 10), -1)  # 최댓값보다 큰 값

    def test_edge_cases(self):
        # 엣지 케이스
        self.assertEqual(binary_search([], 5), -1)  # 빈 배열
        self.assertEqual(binary_search([1], 1), 0)  # 원소가 하나인 배열
        # 중복된 값이 있는 배열에서는 해당 값을 가진 아무 인덱스나 반환해도 됨
        result = binary_search([1, 1, 1, 1], 1)
        self.assertTrue(0 <= result < 4 and [1, 1, 1, 1][result] == 1)

    def test_large_arrays(self):
        # 큰 배열
        large_arr = list(range(0, 10000, 2))  # 0부터 9998까지의 짝수
        self.assertEqual(binary_search(large_arr, 9998), 4999)  # 마지막 원소
        self.assertEqual(binary_search(large_arr, 5000), 2500)  # 중간 근처 값
        self.assertEqual(binary_search(large_arr, 9999), -1)  # 존재하지 않는 값


if __name__ == "__main__":
    unittest.main(verbosity=2)
