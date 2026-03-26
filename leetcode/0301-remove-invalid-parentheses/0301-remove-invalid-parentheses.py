class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.longest = float('-inf')
        self.result = set()

        def dfsBacktrack(parentheses, indx, leftCount, rightCount):
            if indx < len(s):
                current_char = s[indx]
                if current_char == '(':
                    parentheses.append(current_char)
                    dfsBacktrack(parentheses, indx + 1, leftCount + 1, rightCount)
                    parentheses.pop()

                    dfsBacktrack(parentheses, indx + 1, leftCount, rightCount)

                elif current_char == ')':
                    dfsBacktrack(parentheses, indx + 1, leftCount, rightCount)

                    if leftCount > rightCount:
                        parentheses.append(current_char)
                        dfsBacktrack(parentheses, indx + 1, leftCount, rightCount + 1)
                        parentheses.pop()

                else:
                    parentheses.append(current_char)
                    dfsBacktrack(parentheses, indx + 1, leftCount, rightCount)
                    parentheses.pop()

            else:
                if leftCount == rightCount:
                    if len(parentheses) > self.longest:
                        self.longest = len(parentheses)
                        self.result = set()

                        self.result.add("".join(parentheses))
                        
                    elif len(parentheses) == self.longest:
                        self.result.add("".join(parentheses))
        
        dfsBacktrack([], 0, 0, 0)
        return list(self.result)