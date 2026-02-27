n, s = map(int, input().split())

a = list(map(int, input().split()))

ans = 0
curr_sum = 0
r = 0

for l in range(n):
    while r < n and curr_sum < s:
        curr_sum += a[r]
        r += 1
    if curr_sum >= s:
        ans += n - r + 1
    curr_sum -= a[l]

print(ans)
