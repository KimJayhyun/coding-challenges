from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        def getArea(height, left, right):
            now_height = height[left] if height[left] < height[right] else height[right]

            if left + 1 == right:
                return now_height

            mid = left + (right - left) // 2

            left_half_area = getArea(height, left, mid)
            right_half_area = getArea(height, mid, right)
            now_area = now_height * (right - left)

            return max(now_area, left_half_area, right_half_area)

        max_area = 0

        left = 0
        right = len(height) - 1

        area = getArea(height, left, right)
        print(area)

        return max_area


solution = Solution()
print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(solution.maxArea([1, 1]))
