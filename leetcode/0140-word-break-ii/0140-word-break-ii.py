class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        curr_word = []
        result = []

        def dfsBacktrack(i):
            if i == len(s):
                result.append(" ".join(curr_word))
                return

            for k in range(i, len(s)):
                word = s[i:k+1]

                if word in wordDict:
                    curr_word.append(word)
                    dfsBacktrack(k + 1)
                    curr_word.pop()

        dfsBacktrack(0)
        return result