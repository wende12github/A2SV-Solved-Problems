class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d, miss = -1, -1
        
        for i in range(1, len(nums) + 1):
            count = nums.count(i)
            if count == 2:
                d = i
            elif count == 0:
                miss = i
        
        return [d, miss]