import unittest
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1

        return candidate


class TestMajorityElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_majority_element(self):
        self.assertEqual(self.solution.majorityElement([3, 3, 4, 2, 3, 3, 3]), 3)
        self.assertEqual(self.solution.majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)
        self.assertEqual(self.solution.majorityElement([1, 1, 1, 2, 2]), 1)
        self.assertEqual(self.solution.majorityElement([5, 5, 5, 5, 1, 2, 5]), 5)
        self.assertEqual(self.solution.majorityElement([7]), 7)  # 단일 원소

    def test_large_input(self):
        self.assertEqual(self.solution.majorityElement([1] * 1000000 + [2] * 499999), 1)


if __name__ == "__main__":
    unittest.main()
