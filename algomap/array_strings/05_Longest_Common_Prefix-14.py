from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        idx = 0
        prefix = ""

        while True:
            if not idx < len(strs[0]):
                return prefix

            idx_th_prefix = strs[0][idx]

            for i in range(1, len(strs)):
                string = strs[i]

                if not idx < len(string):
                    return prefix

                if not idx_th_prefix == string[idx]:
                    return prefix

            prefix += idx_th_prefix
            idx += 1

        return prefix


solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
