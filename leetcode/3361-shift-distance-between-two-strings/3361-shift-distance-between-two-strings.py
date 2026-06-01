class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        result = 0
        for i in range(len(s)):
            start = ord(s[i]) - ord('a')
            end = ord(t[i]) - ord('a')
            if start == end: continue

            forward = (end - start + 26) % 26
            ford_cost = 0
            for j in range(forward):
                ford_cost += nextCost[(start+j)%26]

            backward = (start - end + 26) % 26
            back_cost = 0
            for j in range(backward):
                back_cost += previousCost[(start-j)%26]

            result += min(ford_cost, back_cost)
        return result