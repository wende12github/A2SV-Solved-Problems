arr = [[0]*5 for _ in range(5)]

left, right = 0, 0

for i in range(5):
    arr[i] = list(map(int, input().split()))
    for j in range(5):
        if arr[i][j] == 1:
            left, right = i, j
print(abs(left-2) + abs(right-2))
