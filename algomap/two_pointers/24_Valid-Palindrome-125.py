class Solution:
    def isPalindrome(self, s: str) -> bool:

        result = []

        differ = ord("a") - ord("A")

        for char in s:
            ascii_char = ord(char)

            if ord("a") <= ascii_char and ascii_char <= ord("z"):
                result.append(char)

            elif ord("A") <= ascii_char and ascii_char <= ord("Z"):
                result.append(chr(ascii_char + differ))

            elif ord("0") <= ascii_char and ascii_char <= ord("9"):
                result.append(char)

        left = 0
        right = len(result) - 1

        while left < right:
            left_char = result[left]
            right_char = result[right]

            if not left_char == right_char:
                return False

            left += 1
            right -= 1

        return True


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(" "))
print(solution.isPalindrome("0P"))
print(solution.isPalindrome("a"))
