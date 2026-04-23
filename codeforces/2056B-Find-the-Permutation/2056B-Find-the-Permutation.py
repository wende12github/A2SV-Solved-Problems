import sys
from functools import cmp_to_key
input = sys.stdin.readline

def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input().strip())
        
        g = [input().strip() for _ in range(n)]
        
        def compare(u, v):
            val_u, val_v = u + 1, v + 1
            
            if val_u < val_v:
                return -1 if g[u][v] == '1' else 1
            else:
                return 1 if g[v][u] == '1' else -1

        p = list(range(n))
        p.sort(key=cmp_to_key(compare))
        
        result = []
        for i in p:
            result.append(i+1)
            
        print(*result)

if __name__ == "__main__":
    main()