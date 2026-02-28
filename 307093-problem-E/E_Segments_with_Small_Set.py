from collections import defaultdict

n, k = map(int, input().split())

arr = list(map(int, input().split()))

freq = defaultdict(int)

left = 0
distinct = 0
answer = 0

for right in range(n):
    if freq[arr[right]] == 0:
        distinct += 1
    freq[arr[right]] += 1

    while distinct > k:
        freq[arr[left]] -= 1
        if freq[arr[left]] == 0:
            distinct -= 1
        left += 1

    answer += (right - left + 1)

print(answer)
