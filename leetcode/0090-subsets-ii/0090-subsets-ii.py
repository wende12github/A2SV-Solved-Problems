class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset = []
        cur = []

        def dfsBacktrack(indx):
            subset.append(cur[:])

            for i in range(indx, len(nums)):

                if i > indx and nums[i] == nums[i-1]:
                    continue

                cur.append(nums[i])
                dfsBacktrack(i + 1)
                cur.pop()

        dfsBacktrack(0)
        return subset