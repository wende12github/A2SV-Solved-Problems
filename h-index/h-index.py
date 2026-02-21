class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()

        for i in range(1, n + 1):
            if citations[n - i] < i:
                return i - 1
                
        return n
