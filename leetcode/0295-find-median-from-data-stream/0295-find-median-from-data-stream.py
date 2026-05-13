class MedianFinder:

    def __init__(self):
        self.min_h, self.max_h = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_h, -1 * num)

        if (self.min_h and self.max_h and (-1 * self.min_h[0]) > self.max_h[0]):
            val = -1 * heapq.heappop(self.min_h)
            heapq.heappush(self.max_h, val)

        if len(self.min_h) > len(self.max_h) + 1:
            val = -1 * heapq.heappop(self.min_h)
            heapq.heappush(self.max_h, val)
        
        if len(self.max_h) > len(self.min_h) + 1:
            val = heapq.heappop(self.max_h)
            heapq.heappush(self.min_h, -1 * val)
        
    def findMedian(self) -> float:
        if len(self.min_h) > len(self.max_h):
            return float(-1 * self.min_h[0])

        if len(self.max_h) > len(self.min_h):
            return float(self.max_h[0])
        
        return (-1 * self.min_h[0] + self.max_h[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()