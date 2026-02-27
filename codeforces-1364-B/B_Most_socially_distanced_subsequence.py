t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    result = [arr[0]]
    for i in range(1, n-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            result.append(arr[i])
        if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
            result.append(arr[i])
            
    result.append(arr[n-1])
    print(len(result))
    print(*result)
