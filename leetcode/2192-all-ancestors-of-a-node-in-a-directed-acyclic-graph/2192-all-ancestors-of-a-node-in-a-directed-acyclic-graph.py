class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        
        for f_edge, t_edge in edges:
            graph[t_edge].append(f_edge)

        def dfs(curr_node, visited):
            visited.add(curr_node)
            for nebor in graph[curr_node]:
                if nebor not in visited:
                    dfs(nebor, visited)

        result = []
        for i in range(n):
            current = []
            visited = set()
            dfs(i, visited)

            for node in range(n):
                if node != i:
                    if node in visited:
                        current.append(node)
            result.append(current)

        return result