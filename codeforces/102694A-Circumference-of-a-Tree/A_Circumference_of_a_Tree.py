import sys
from collections import deque

# REMOVED: sys.setrecursionlimit(300005) to save massive stack memory

input = sys.stdin.readline

def main():
    try:
        line = input().split()
        if not line: return
        n = int(line[0])
    except (EOFError, IndexError):
        return

    if n <= 1:
        print(0)
        return
    
    # Pack integers into a single 1D list to reduce object overhead
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # Reuse a single global distance array to prevent double allocation
    dist = [-1] * (n + 1)

    def bfs(start):
        # Reset the array values instead of re-allocating memory
        for i in range(n + 1):
            dist[i] = -1
            
        dist[start] = 0
        queue = deque([start])
        far_node = start
        max_dist = 0
        
        while queue:
            node = queue.popleft()
            curr_dist = dist[node]
            
            for nebr in graph[node]:
                if dist[nebr] == -1:
                    d = curr_dist + 1
                    dist[nebr] = d
                    queue.append(nebr)
                    
                    if d > max_dist:
                        max_dist = d
                        far_node = nebr
                        
        return far_node, max_dist

    u, _ = bfs(1)
    _, dim = bfs(u)
    
    print(dim * 3)

if __name__ == "__main__":
    main()
