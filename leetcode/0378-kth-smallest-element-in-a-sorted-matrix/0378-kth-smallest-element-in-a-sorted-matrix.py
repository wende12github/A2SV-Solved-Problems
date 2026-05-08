class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for mat in matrix:
            for m in mat:
                heapq.heappush(heap, -(m))
                if len(heap) > k:
                    heapq.heappop(heap)

        return -heap[0]