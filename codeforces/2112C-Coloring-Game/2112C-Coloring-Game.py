t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    
    count = 0    
    max_k = array[-1]
    
    for i in range(2, n):
        k = array[i]
        l, r = 0, i - 1
        
        while l < r:
            current_sum = array[l] + array[r]
            if current_sum > k and current_sum + k > max_k:
                count += r - l
                r -= 1
            else:
                l += 1
                
    print(count)