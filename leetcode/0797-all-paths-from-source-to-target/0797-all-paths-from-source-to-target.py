class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        
        def dfs(path, idx):
                if idx == n-1:
                    result.append(list(path))
                    return 

                for i in graph[idx]:
                    path.append(i)
                    dfs(path, i)
                    path.pop()
                    
        result = []
        dfs([0], 0)
        return result