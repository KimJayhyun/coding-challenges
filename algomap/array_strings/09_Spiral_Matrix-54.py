from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x_end = len(matrix) - 1
        y_end = len(matrix[0]) - 1

        x_start = 0
        y_start = 0

        x = 0
        y = 0

        direction = 1
        result = []

        count = 0
        max_count = len(matrix) * len(matrix[0])
        while True:
            if direction == 1:  # 우측으로 이동
                while y_start <= y and y <= y_end:
                    result.append(matrix[x][y])
                    count += 1
                    y += 1

                y -= 1
                x += 1

                x_start += 1
                direction = 2

            elif direction == 2:  # 아래로 이동
                while x_start <= x and x <= x_end:
                    result.append(matrix[x][y])
                    count += 1
                    x += 1
                x -= 1
                y -= 1

                y_end -= 1
                direction = -1

            elif direction == -1:  # 좌측으로 이동
                while y_start <= y and y <= y_end:
                    result.append(matrix[x][y])
                    count += 1
                    y -= 1
                y += 1
                x -= 1

                x_end -= 1
                direction = -2
            elif direction == -2:  # 위로 이동
                while x_start <= x and x <= x_end:
                    result.append(matrix[x][y])
                    count += 1
                    x -= 1
                x += 1
                y += 1

                y_start += 1
                direction = 1

            if count == max_count:
                break

        return result


# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

#         m = len(matrix)
#         n = len(matrix[0])

#         length = m * n
#         step = 0

#         res = []

#         seen = set()
#         dxdy = 0

#         x, y = 0, 0
#         while step < length:
#             if x >= m or y >= n or x < 0 or y < 0 or (x, y) in seen:

#                 x -= directions[dxdy][0]
#                 y -= directions[dxdy][1]

#                 dxdy += 1
#                 if dxdy == len(directions):
#                     dxdy = 0
#                 x += directions[dxdy][0]
#                 y += directions[dxdy][1]


#             seen.add((x, y))
#             res.append(matrix[x][y])

#             x += directions[dxdy][0]
#             y += directions[dxdy][1]


#             step += 1

#         return res


solution = Solution()
print(solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
