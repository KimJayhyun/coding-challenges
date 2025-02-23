# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         from collections import Counter

#         text_counter = Counter(text)
#         balloons_counter = Counter("balloon")

#         balloons_count = 0

#         while True:
#             for item, count in balloons_counter.items():
#                 if text_counter[item] < count:
#                     return balloons_count

#             text_counter = text_counter - balloons_counter
#             balloons_count += 1


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter

        text_counter = Counter(text)
        ballon = "balloon"

        if any(char not in text_counter for char in ballon):
            return 0
        else:
            return min(
                text_counter["b"],
                text_counter["a"],
                text_counter["l"] // 2,
                text_counter["o"] // 2,
                text_counter["n"],
            )


solution = Solution()
print(solution.maxNumberOfBalloons("nlaebolko"))
print(solution.maxNumberOfBalloons("loonbalxballpoon"))
print(solution.maxNumberOfBalloons("leetcode"))
