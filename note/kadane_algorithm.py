import unittest


def kadane_with_subarray(arr):
    if not arr:  # 빈 배열 처리
        return 0, []

    max_sum = float("-inf")
    current_sum = 0
    start = end = s = 0

    for i, num in enumerate(arr):
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
            start, end = s, i  # 최댓값이 갱신될 때마다 시작, 끝 인덱스 갱신

        if current_sum < 0:
            current_sum = 0
            s = i + 1  # 새로운 부분합을 시작할 위치 저장

    return max_sum, arr[start : end + 1]


class TestKadaneWithSubarray(unittest.TestCase):
    def test_default_case(self):
        self.assertEqual(
            kadane_with_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), (6, [4, -1, 2, 1])
        )

    def test_all_positive(self):
        self.assertEqual(kadane_with_subarray([1, 2, 3, 4, 5]), (15, [1, 2, 3, 4, 5]))

    def test_all_negative(self):
        self.assertEqual(kadane_with_subarray([-1, -2, -3, -4]), (-1, [-1]))

    def test_mixed_numbers(self):
        self.assertEqual(
            kadane_with_subarray([-2, -3, 4, -1, -2, 1, 5, -3]), (7, [4, -1, -2, 1, 5])
        )

    def test_single_element(self):
        self.assertEqual(kadane_with_subarray([5]), (5, [5]))
        self.assertEqual(kadane_with_subarray([-5]), (-5, [-5]))

    def test_empty_array(self):
        self.assertEqual(kadane_with_subarray([]), (0, []))


if __name__ == "__main__":
    unittest.main()
