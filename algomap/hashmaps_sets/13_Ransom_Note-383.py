class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter

        magazine_table = Counter(magazine)

        for char in ransomNote:
            if magazine_table[char] == 0:
                return False

            magazine_table[char] -= 1

        return True
