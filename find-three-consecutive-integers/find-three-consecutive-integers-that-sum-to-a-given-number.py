class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        result = []

        if (num - 3) % 3 == 0:
            x = (num - 3) // 3
            result.append(x)
            result.append(x+1)
            result.append(x+2)

        return result
