from typing import List

# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:

#         left = 0
#         right = 1

#         result = []
#         while left < len(intervals):
#             merge_interval = intervals[left]

#             while right < len(intervals):
#                 flag = 0
#                 left_start_num, left_last_num = merge_interval
#                 interval = intervals[right]

#                 right_start_num, right_last_num = interval

#                 if left_start_num < right_start_num:
#                     if right_start_num <= left_last_num <= right_last_num:
#                         merge_interval = [left_start_num, right_last_num]
#                         flag = 1
#                     elif right_last_num <= left_last_num:
#                         merge_interval = [left_start_num, left_last_num]
#                         flag = 1
#                 else:  # right_start_num < left_start_num
#                     if left_start_num <= right_last_num <= left_last_num:
#                         merge_interval = [right_start_num, left_last_num]
#                         flag = 1
#                     elif left_last_num <= right_last_num:
#                         merge_interval = [right_start_num, right_last_num]
#                         flag = 1

#                 if flag == 0:
#                     break

#                 right += 1

#             result.append(merge_interval)
#             left = right
#             right = left + 1

#         return result


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for idx in range(1, len(intervals)):
            last_end = result[-1][1]
            start, end = intervals[idx]

            if start <= last_end:
                result[-1][1] = max(last_end, end)
            else:
                result.append([start, end])

        return result


solution = Solution()
print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(solution.merge([[1, 4], [4, 5]]))
print(solution.merge([[1, 4], [0, 2], [3, 5]]))
