from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0

        left = 0
        right = len(height) - 1

        while left < right:
            w = right - left
            h = min(height[right], height[left])

            max_area = max(max_area, w * h)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_area


solution = Solution()
print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(solution.maxArea([1, 1]))
