class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = {}
        res = []
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for key, value in count.items():
            if value > n/3:
                res.append(key)
        return res
