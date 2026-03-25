class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def backtrack(start, combination):
            if len(combination) == k:
                combinations.append(combination[:])
                return

            for num in range(start, n + 1):
                combination.append(num)
                backtrack(num + 1, combination)
                combination.pop()
            
        backtrack(1, [])

        return combinations