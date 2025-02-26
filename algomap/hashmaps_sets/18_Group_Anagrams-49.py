from typing import List

## O(n * m lon m)
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         from collections import Counter, defaultdict

#         anagram_dict = defaultdict(list)
#         for s in strs:
#             key = "".join(sorted(s))
#             anagram_dict[key].append(s)


#         return list(anagram_dict.values())


## O(n * m)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter, defaultdict

        anagram_dict = defaultdict(list)
        for s in strs:
            char_count = [0] * 26

            for char in s:
                char_count[ord(char) - ord("a")] += 1

            anagram_dict[tuple(char_count)].append(s)


        return list(anagram_dict.values())


solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams([""]))
print(solution.groupAnagrams(["a"]))
