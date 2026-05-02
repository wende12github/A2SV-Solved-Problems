class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for _ in range(len(graph))]

        def dfs(node):
            
            for num in graph[node]:
                if color[num] == -1:
                    if color[node] == 0:
                        color[num] = 1
                    else:
                        color[num] = 0
                    if not dfs(num):
                        return False
                elif color[num] == color[node]:
                    return False
            return True

        for node in range(len(graph)):
            if color[node] == -1:
                color[node] = 0
                if not dfs(node):
                    return False

        return True