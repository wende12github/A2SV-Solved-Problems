class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mapp = {}
        result = []
        for word in words:
            mapp[word] = mapp.get(word, 0) + 1
        
        min_heap = []
        for word, count in mapp.items():
            min_heap.append((-count, word))
        heapq.heapify(min_heap)

        print(min_heap)
        for i in range(k):
            result.append(heapq.heappop(min_heap)[1])

        return result
