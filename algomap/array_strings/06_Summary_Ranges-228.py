from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        result = []

        left = 0

        while left < len(nums):
            start = nums[left]

            right = left + 1
            shift = 1
            while True:
                if right >= len(nums):
                    break

                if start + shift == nums[right]:
                    right += 1
                    shift += 1
                else:
                    break
            right -= 1

            if left == right:
                result.append(str(start))
            else:
                result.append(f"{start}->{nums[right]}")

            left = right + 1

        return result


solution = Solution()
print(solution.summaryRanges([0, 1, 2, 4, 5, 7]))
print(solution.summaryRanges([0, 2, 3, 4, 6, 8, 9]))
