import heapq
import sys

input = sys.stdin.readline

def main():
    n = int(input())
    
    heap = []
    result = []

    for i in range(1, n + 1):
        strs = input().split()
        command = strs[0]

        if command == 'insert':
            x = int(strs[1])
            heapq.heappush(heap, x)
            result.append(f"insert {x}")

        elif command == 'removeMin':
            if not heap:
                result.append("insert 0")
            else:
                heapq.heappop(heap)
            result.append("removeMin")

        elif command == 'getMin':
            x = int(strs[1])
            while heap and heap[0] < x:
                heapq.heappop(heap)
                result.append("removeMin")
            
            if not heap or heap[0] > x:
                heapq.heappush(heap, x)
                result.append(f"insert {x}")
            
            result.append(f"getMin {x}")

    print(len(result))
    print('\n'.join(result))

if __name__ == "__main__":
    main()