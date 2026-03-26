class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def backtrack(subset, indx):
            subsets.append(subset[:])

            for i in range(indx, len(nums)):
                subset.append(nums[i])
                backtrack(subset, i+1)
                subset.pop()

        backtrack([], 0)
        return subsets