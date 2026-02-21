import sys


def bubble_sort(result, arr, val):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                result.append((val, j + 1))
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped: break
    return result    


if __name__ == "__main__":
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n = int(input())
        a_arr = list(map(int, input().split()))
        b_arr = list(map(int, input().split()))

        result = []
            
        for i in range(n):
            if a_arr[i] > b_arr[i]:
                result.append((3, i + 1))
                a_arr[i], b_arr[i] = b_arr[i], a_arr[i]       
                
        bubble_sort(result, a_arr, 1)
        bubble_sort(result, b_arr, 2)

        print(len(result))
        for op_type, pos in result:
            print(op_type, pos)
