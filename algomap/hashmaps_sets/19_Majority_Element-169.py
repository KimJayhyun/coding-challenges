from typing import List

## Time: O(n)
## Space : O(n)
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         from collections import defaultdict

#         counter = defaultdict(int)
#         n = len(nums)

#         for num in nums:
#             counter[num] += 1

#             if counter[num] >= n // 2 + 1:
#                 return num


## Boyer-Moore Voting Algorithm
## Time: O(n)
## Space: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            count += 1 if candidate == num else -1

        return candidate


solution = Solution()
print(solution.majorityElement([3, 2, 3]))
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
