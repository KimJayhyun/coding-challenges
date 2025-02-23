from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         from collections import defaultdict

#         nums_dict = defaultdict(int)

#         for idx, num in enumerate(nums):
#             nums_dict[num] = idx

#         for idx, num in enumerate(nums):
#             remainder = target - num

#             if remainder in nums_dict and idx != nums_dict[remainder]:
#                 return [idx, nums_dict[remainder]]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict

        nums_dict = defaultdict(int)

        for idx, num in enumerate(nums):
            remainder = target - num

            if remainder in nums_dict:
                return [idx, nums_dict[remainder]]

            nums_dict[num] = idx


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([3, 2, 4], 6))
print(solution.twoSum([3, 3], 6))
