class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0
        right_value = 0

        for char in s[::-1]:
            left_value = roman_numerals[char]
            if left_value < right_value:
                total -= left_value
            else:
                total += left_value

            right_value = left_value
        return total


solution = Solution()
print(solution.romanToInt("III"))
print(solution.romanToInt("LVIII"))
print(solution.romanToInt("MCMXCIV"))
