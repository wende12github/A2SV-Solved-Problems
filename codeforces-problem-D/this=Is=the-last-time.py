import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    casinos = [tuple(map(int, input().split())) for _ in range(n)]
    
    casinos.sort()
    
    curr = k
    for l, r, real in casinos:
        if l > curr:
            break
        if l <= curr <= r:
            curr = max(curr, real)
    
    print(curr)
