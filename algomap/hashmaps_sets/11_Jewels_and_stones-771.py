class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import defaultdict

        result = 0
        stones_table = defaultdict(int)

        for s in stones:
            stones_table[s] += 1

        for j in jewels:
            result += stones_table[j]

        return result


solution = Solution()
print(solution.numJewelsInStones("aA", "aAAsbvcv"))
print(solution.numJewelsInStones("z", "ZZ"))
