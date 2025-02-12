from typing import List

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:

#         result = [0 for _ in range(len(nums))]
#         forward_product = [nums[0] for _ in range(len(nums))]
#         backward_product = [nums[-1] for _ in range(len(nums))]

#         for idx in range(1, len(nums)):
#             forward_product[idx] = nums[idx] * forward_product[idx - 1]

#         for idx in range(len(nums) - 2, -1, -1):
#             backward_product[idx] = nums[idx] * backward_product[idx + 1]

#         for idx in range(len(nums)):
#             if idx == 0:
#                 result[idx] = backward_product[1]
#             elif idx == len(nums) - 1:
#                 result[idx] = forward_product[-2]
#             else:
#                 result[idx] = forward_product[idx - 1] * backward_product[idx + 1]

#         return result


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1 for _ in range(len(nums))]

        prev_product = 1
        post_product = 1

        for idx in range(len(nums)):
            result[idx] *= prev_product
            prev_product *= nums[idx]

        for idx in range(len(nums) - 1, -1, -1):
            result[idx] *= post_product
            post_product *= nums[idx]

        return result


solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))
