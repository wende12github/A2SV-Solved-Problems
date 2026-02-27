
n, s = map(int, input().split())

nums = list(map(int, input().split()))
left = 0
current_sum = 0
count = 0

for right in range(n):
    current_sum += nums[right]

    while current_sum > s and left <= right:
        current_sum -= nums[left]
        left += 1

    count += right - left + 1

print(count)
