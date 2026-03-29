class Solution:
    def splitString(self, s: str) -> bool:
        current_split = []
        def dfsBacktrack(indx):
            if indx >= len(s):
                return len(current_split) >= 2

            for i in range(indx, len(s)):
                cur_val = int(s[indx:i+1])

                if len(current_split) == 0 or cur_val == current_split[-1] - 1:
                    current_split.append(cur_val)

                    if dfsBacktrack(i + 1):
                        return True

                    current_split.pop()
            return False

        return dfsBacktrack(0)