class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(wage)
        total_cost = float('inf')
        curr_q = 0
        wage_quality_r = []

        for i in range(n):
            wage_quality_r.append([wage[i] / quality[i], quality[i]])
        print(wage_quality_r)
        wage_quality_r.sort()

        heap =  []
        for i in range(n):
            heapq.heappush(heap, -wage_quality_r[i][1])
            curr_q += wage_quality_r[i][1]

            if len(heap) > k:
                curr_q += heapq.heappop(heap)
            
            if len(heap) == k:
                total_cost = min(total_cost, curr_q * wage_quality_r[i][0])

        return total_cost