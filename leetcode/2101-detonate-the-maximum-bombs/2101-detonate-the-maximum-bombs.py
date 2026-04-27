from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(bombs)
        visited = set()

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                x = bombs[i][0] - bombs[j][0]
                y = bombs[i][1] - bombs[j][1]
                if bombs[i][2] >= math.sqrt((x**2) + (y**2)):
                    graph[i].append(j)

        def dfs(node):
            for nod in graph[node]:
                if nod not in visited:
                    visited.add(nod)
                    dfs(nod)

        cnt = 0
        for i in range(n):
            visited = set([i])

            dfs(i)
            cnt = max(cnt, len(visited))

        return cnt