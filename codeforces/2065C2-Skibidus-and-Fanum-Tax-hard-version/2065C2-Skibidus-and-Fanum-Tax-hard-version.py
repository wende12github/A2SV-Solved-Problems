from bisect import bisect_left

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    b.sort()
    
    first_num = min(a[0], b[0] - a[0])
    possible = True
    
    for i in range(1, n):
        curr_1 = a[i] if a[i] >= first_num else float('inf')
        
        num = first_num + a[i]
        p = bisect_left(b, num)
        
        curr_2 = float('inf')
        if p < m:
            curr_2 = b[p] - a[i]
            
            
        curr = min(curr_1, curr_2)
        
        if curr == float('inf'):
            possible = False
            break
        first_num = curr
        
    if possible:
        print("YES")
    else:
        print("NO")