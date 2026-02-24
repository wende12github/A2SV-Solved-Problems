from collections import  Counter

t = int(input())
for _ in range(t):
    a_str = input()
    b_str = input()

    s_count = Counter(a_str)
    t_count = Counter(b_str)
    possible = True
    for key in s_count:
        if s_count[key] > t_count[key]:
            possible = False
            break
        
    if not possible:
        print("Impossible")
        continue
    
    for k in s_count:
        t_count[k] -= s_count[k]
        
    rem = []
    for key, val in t_count.items():
        rem.extend([key]*val)
    rem.sort()
    
    i, j = 0, 0
    
    result = []
    while i < len(rem) and j < len(a_str):
        if rem[i] < a_str[j]:
            result.append(rem[i])
            i += 1
        else:
            result.append(a_str[j])
            j += 1
            
    result.extend(a_str[j:])
    result.extend(rem[i:])
    
    print("".join(result))
