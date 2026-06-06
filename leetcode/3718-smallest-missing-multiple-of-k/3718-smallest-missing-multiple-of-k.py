class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = k
        for num in nums:
            if num == res:
                res += k

        return res