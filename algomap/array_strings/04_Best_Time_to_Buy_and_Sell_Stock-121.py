from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:  # 빈 배열 처리
            return 0

        min_price = float("inf")  # 초기 최소 가격 (무한대)
        max_profit = 0  # 최대 이익

        for price in prices:
            min_price = min(min_price, price)  # 현재까지의 최저 주가 갱신
            max_profit = max(max_profit, price - min_price)  # 최대 이익 갱신

        return max_profit


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         pre_sum = [0 for _ in range(len(prices))]

#         for idx in range(1, len(prices)):
#             pre_sum[idx] = prices[idx] - prices[idx - 1]

#         max_profit = float("-inf")
#         current_profit = 0
#         for num in pre_sum:
#             current_profit += num
#             max_profit = max(max_profit, current_profit)

#             if current_profit < 0:
#                 current_profit = 0

#         return max_profit


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
print(solution.maxProfit([7, 6, 4, 3, 1]))
