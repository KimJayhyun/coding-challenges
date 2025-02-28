from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)
        square_list = [0] * n

        left = 0
        right = n - 1
        pos = n - 1

        while left <= right:
            left_num = nums[left] * nums[left]
            right_num = nums[right] * nums[right]

            if left_num < right_num:
                square_list[pos] = right_num
                right -= 1
                pos -= 1

            elif left_num >= right_num:
                square_list[pos] = left_num
                left += 1
                pos -= 1

        return square_list


solution = Solution()
print(solution.sortedSquares([-4, -1, 0, 3, 10]))
print(solution.sortedSquares([-7, -3, 2, 3, 11]))
