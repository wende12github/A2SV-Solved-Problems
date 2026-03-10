class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*(len(temperatures))

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                indx = stack.pop()
                result[indx] = i - indx

            stack.append(i)

        return result