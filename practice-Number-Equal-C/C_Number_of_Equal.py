
n, s = map(int, input().split())

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

i = j = 0
result = 0

while i < n and j < s:
    if nums1[i] < nums2[j]:
        i += 1
    elif nums1[i] > nums2[j]:
        j += 1
    else:
        val = nums1[i]
        cnt_a = 0
        while i < n and nums1[i] == val:
            cnt_a += 1
            i += 1

        cnt_b = 0
        while j < s and nums2[j] == val:
            cnt_b += 1
            j += 1

        result += cnt_a * cnt_b

print(result)
