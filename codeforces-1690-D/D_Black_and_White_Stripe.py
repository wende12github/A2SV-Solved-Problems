t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    strs = input().strip()
    
    w_cnt = 0
    for i in range(k):
        if strs[i] == 'W':
            w_cnt += 1
            
    min_w = w_cnt
    for r in range(k, n):
        left = r - k
        
        if strs[left] == 'W':
            w_cnt -= 1
        
        if strs[r] == 'W':
            w_cnt += 1
        
        min_w = min(min_w, w_cnt)
    print(min_w)
