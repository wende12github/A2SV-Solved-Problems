class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # [3, 2, 4, 1]
        # [1, 4, 2, 3]  4
        # [4, 1, 2, 3]  2
        # [3, 2, 1, 4]  4
        # [1, 2, 3, 4]  3
        resualt = []
        n = len(arr)

        for i in range(n, 0, -1):
            for j in range(n):
                if arr[j] == i:
                    for k in range((j+1) // 2):
                        arr[k], arr[j-k] = arr[j-k], arr[k]
                    
                    for k in range(i // 2):
                        arr[k], arr[i-k-1] = arr[i-k-1], arr[k]
                    
                    resualt.append(j+1)
                    resualt.append(i)
                    break
        return resualt
