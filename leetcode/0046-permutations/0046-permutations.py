class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfsBacktrack(num):
            if len(num) == len(nums):
                result.append(num[:])
                return

            for i in range(len(nums)):
                if nums[i] in num:
                    continue
                    
                num.append(nums[i])
                dfsBacktrack(num)
                num.pop()


        dfsBacktrack([])
        return result