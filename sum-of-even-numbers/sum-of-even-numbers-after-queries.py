class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even = sum([v for v in nums if v % 2 == 0])
        result = []

        for val, indx in queries:
            if nums[indx] % 2 == 0:
                even -= nums[indx]
            nums[indx] += val
            
            if nums[indx] % 2 == 0:
                even += nums[indx]
            result.append(even)

        return result
