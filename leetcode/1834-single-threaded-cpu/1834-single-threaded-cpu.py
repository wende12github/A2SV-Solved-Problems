class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        m_t = float('inf')

        for i, task in enumerate(tasks):
            if task[0] < m_t:
                m_t = task[0]
            task.append(i)
        tasks.sort()
        result = []
        min_heap = []
        i = 0

        while min_heap or i < len(tasks):
            while i < len(tasks) and m_t >= tasks[i][0]:
                heapq.heappush(min_heap, [tasks[i][1], tasks[i][2]])
                i += 1
            if not min_heap:
                m_t = tasks[i][0]
            else:
                p, indx = heapq.heappop(min_heap)
                m_t += p
                result.append(indx)

        return result
