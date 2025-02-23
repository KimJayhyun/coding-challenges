class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)
