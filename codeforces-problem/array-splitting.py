import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = list(map(int, input().split()))
max_r = arr[-1] - arr[0]

temp = []
for i in range(len(arr)-1):
    temp.append(arr[i+1] - arr[i])
    
temp.sort(reverse=True)

for j in range(k-1):
    max_r -= temp[j]
print(max_r)
