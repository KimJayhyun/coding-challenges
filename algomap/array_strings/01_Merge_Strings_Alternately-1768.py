class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []

        len_word1 = len(word1)
        len_word2 = len(word2)
        index = 0

        while True:
            if index == len_word1 or index == len_word2:
                break

            result.append(word1[index])
            result.append(word2[index])

            index += 1

        while index < len_word1:
            result.append(word1[index])
            index += 1

        while index < len_word2:
            result.append(word2[index])
            index += 1

        return "".join(result)
