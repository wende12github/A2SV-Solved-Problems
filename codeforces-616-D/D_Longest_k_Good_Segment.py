import sys
from collections import defaultdict

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
freq = defaultdict(int)

left = 0
distinct = 0

best_len = 0
best_l = 0
best_r = 0

for right in range(n):
    if freq[arr[right]] == 0:
        distinct += 1

    freq[arr[right]] += 1

    while distinct > k:
        freq[arr[left]] -= 1
        if freq[arr[left]] == 0:
            distinct -= 1
        left += 1

    if right - left + 1 > best_len:
        best_len = right - left + 1
        best_l = left
        best_r = right

print(best_l + 1, best_r + 1)
