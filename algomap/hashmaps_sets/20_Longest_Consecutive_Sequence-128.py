from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # 시작점이 될 수 있는 조건
            # num-1이 존재하지 않으면 num이 시작점
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest


solution = Solution()
print(solution.longestConsecutive([3, 2, 3]))
print(solution.longestConsecutive([2, 2, 1, 1, 1, 2, 2]))
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(solution.longestConsecutive([1, 0, 1, 2]))
