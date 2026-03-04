n, k, q = map(int, input().split())
MAX_VAL = 200000

diff = [0] * (MAX_VAL + 2)
for i in range(n):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r+1] -= 1

cover = [0] * (MAX_VAL + 2)
current = 0

for i in  range(1, MAX_VAL + 1):
    current += diff[i]
    cover[i] = current
    
pref = [0] * (MAX_VAL + 2)
for i in range(1, MAX_VAL + 1):
    if cover[i] >= k:
        pref[i] = pref[i - 1] + 1
    else:
        pref[i] = pref[i - 1] + 0

for i in range(q):
    a, b = map(int,input().split())
    print(pref[b] - pref[a - 1])

