n = int(input())
arr = []
cnt_map = {}

for _ in range(n - 1):
    val = int(input())
    arr.append(val)
    cnt_map[val] = cnt_map.get(val, 0) + 1

m = 2
for i in arr:
    if m in cnt_map:
        cnt_map[i] -= 1
    m += 1

result = "Yes"
for count in cnt_map.values():
    if count < 3:
        result = "No"
        break
print(result)