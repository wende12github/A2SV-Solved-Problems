class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = [0]*n
        for pre, nxt in relations:
            graph[pre - 1].append(nxt - 1)
            indegree[nxt - 1] += 1
        
        queue = deque()
        max_time = [0]*n

        for node in range(n):
            if indegree[node] == 0:
                queue.append(node)
                max_time[node] = time[node]
        
        while queue:
            node = queue.popleft()
            for nebor in graph[node]:
                max_time[nebor] = max(max_time[nebor], max_time[node] + time[nebor])
                indegree[nebor] -= 1

                if indegree[nebor] == 0:
                    queue.append(nebor)

        return max(max_time)