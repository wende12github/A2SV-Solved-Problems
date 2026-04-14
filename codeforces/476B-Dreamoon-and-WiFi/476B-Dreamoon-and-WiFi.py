import math

s1 = input()
s2 = input()
ans = 0

result = 0
for s in s1:
    if s == '+':
        result += 1
    else:
        result -= 1

curr = 0
k = 0

for s in s2:
    if s == '+':
        curr += 1
    elif s == '-':
        curr -= 1
    else:
        k += 1
        
dif = result - curr
x = dif + k
y = x / 2
if (abs(dif) > k) or (x % 2 != 0):
    print(f"{ans:.12f}")
else:
    p_need = x // 2
    
    f = math.comb(k, p_need)
    
    total = pow(2, k)
    
    ans = f / total
    print(f"{ans:.12f}")