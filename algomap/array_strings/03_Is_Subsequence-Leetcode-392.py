class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        idx_s = 0

        for word_t in t:
            if word_t == s[idx_s]:
                idx_s += 1

            if idx_s == len(s):
                return True

        return False
