from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter, defaultdict

        anagram_dict = defaultdict(list)
        for s in strs:
            s_counter = Counter(s)

            key = tuple(s_counter)

            anagram_dict[key].append(s)

        print(anagram_dict)
        return anagram_dict.values()


solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams([""]))
print(solution.groupAnagrams(["a"]))
