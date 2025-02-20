from typing import List

## defaultdict 보다 set이 더 빠르다.


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))
print(solution.containsDuplicate([5, 1, 9, 11]))
