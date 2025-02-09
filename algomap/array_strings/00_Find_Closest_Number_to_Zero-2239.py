# https://leetcode.com/problems/find-closest-number-to-zero/
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_num = nums[0]

        for num in nums:
            if (abs(num) < abs(min_num)) or (
                abs(num) == abs(min_num) and num > min_num
            ):
                min_num = num

        return min_num

        # Time: O(n)
        # Space: O(1)
