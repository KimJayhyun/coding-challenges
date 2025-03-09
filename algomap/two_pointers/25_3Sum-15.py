from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result = []

        for idx in range(len(nums)):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            number = nums[idx]

            # Sort 했으므로 현재 `number`가 0 보다 크다면
            # 세 수의 합이 0과 같아질 수 없음
            if number > 0:
                break

            left = idx + 1
            right = len(nums) - 1

            while left < right:
                left_number = nums[left]
                right_number = nums[right]

                total = number + left_number + right_number

                if total == 0:
                    result.append([number, left_number, right_number])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total > 0:
                    right -= 1
                else:
                    left += 1

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
print(solution.threeSum([-2, 0, 1, 1, 2]))
