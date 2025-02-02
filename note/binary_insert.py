import unittest


def find_index_with_binary_search(arr, target):
    if not arr:
        return 0

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return left


class TestFindInsertPosition(unittest.TestCase):
    def test_basic_cases(self):
        # 기본적인 케이스
        self.assertEqual(
            find_index_with_binary_search([1, 3, 5, 7], 4), 2
        )  # 중간에 삽입
        self.assertEqual(
            find_index_with_binary_search([1, 3, 5, 7], 0), 0
        )  # 맨 앞에 삽입
        self.assertEqual(
            find_index_with_binary_search([1, 3, 5, 7], 9), 4
        )  # 맨 뒤에 삽입
        self.assertEqual(
            find_index_with_binary_search([1, 3, 5, 7], 5), 2
        )  # 이미 있는 값

    def test_edge_cases(self):
        # 엣지 케이스
        self.assertEqual(find_index_with_binary_search([], 1), 0)  # 빈 배열
        self.assertEqual(
            find_index_with_binary_search([1], 0), 0
        )  # 한 원소 배열, 앞에 삽입
        self.assertEqual(
            find_index_with_binary_search([1], 2), 1
        )  # 한 원소 배열, 뒤에 삽입
        self.assertEqual(
            find_index_with_binary_search([1], 1), 0
        )  # 한 원소 배열, 같은 값

    def test_duplicate_values(self):
        # 중복값이 있는 경우
        pos = find_index_with_binary_search([1, 1, 1], 1)
        # 어떤 위치든 허용
        self.assertTrue(
            0 <= pos <= 3, f"반환된 위치 {pos}가 유효한 범위를 벗어났습니다"
        )

        pos = find_index_with_binary_search([1, 2, 2, 2, 3], 2)
        self.assertTrue(
            1 <= pos <= 3, f"반환된 위치 {pos}가 유효한 범위를 벗어났습니다"
        )

    def test_large_array(self):
        # 큰 배열
        large_arr = list(range(0, 100, 2))  # [0, 2, 4, ..., 98]
        self.assertEqual(
            find_index_with_binary_search(large_arr, 51), 26
        )  # 중간값 근처
        self.assertEqual(find_index_with_binary_search(large_arr, -1), 0)  # 맨 앞
        self.assertEqual(find_index_with_binary_search(large_arr, 99), 50)  # 맨 뒤

    def test_negative_numbers(self):
        # 음수를 포함한 케이스
        self.assertEqual(find_index_with_binary_search([-5, -3, 0, 2], -4), 1)
        self.assertEqual(find_index_with_binary_search([-5, -3, 0, 2], -6), 0)
        self.assertEqual(find_index_with_binary_search([-5, -3, 0, 2], 1), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
