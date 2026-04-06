class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []

        def dfsBacktrack(indx):
            if len(curr) > 1:
                result.append(curr[:])

            dp = set()

            for i in range(indx, len(nums)):
                if nums[i] in dp or (curr and nums[i] < curr[-1]):
                    continue

                dp.add(nums[i])
                curr.append(nums[i])
                dfsBacktrack(i + 1)
                curr.pop()

        dfsBacktrack(0)
        return result