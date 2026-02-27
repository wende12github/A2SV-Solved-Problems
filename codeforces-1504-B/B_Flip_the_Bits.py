t = int(input())

for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()
    
    balanced = [False] * n
    zeros = ones = 0
    
    for i in range(n):
        if a[i] == '0':
            zeros += 1
        else:
            ones += 1
            
        if zeros == ones:
            balanced[i] = True
            
    flip = 0
    possible = True
    
    for i in range(n - 1, -1, -1):
        current = a[i]
        
        if flip == 1:
            current = '1' if current == '0' else '0'
        
        if current == b[i]:
            continue
        
        if balanced[i]:
            flip ^= 1
        else:
            possible = False
            break
    print("YES" if possible else "NO")
