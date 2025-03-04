from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter

        result = []
        seem_set = set()
        num_counter = Counter(nums)

        for left in range(len(nums) - 1):
            left_number = nums[left]
            for right in range(left + 1, len(nums)):
                right_number = nums[right]

                find_number = 0 - left_number - right_number

                if find_number in num_counter.keys():
                    count = 0

                    if left_number == find_number:
                        count += 1
                    if right_number == find_number:
                        count += 1

                    if num_counter[find_number] > count:
                        seem_item = tuple(
                            sorted([left_number, right_number, find_number])
                        )

                        if not seem_item in seem_set:
                            result.append([left_number, right_number, find_number])
                            seem_set.add(seem_item)

        return result


solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
print(
    solution.threeSum(
        [
            0,
            1,
            1,
        ]
    )
)
print(solution.threeSum([0, 0, 0]))
