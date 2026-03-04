class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rema_f = {0:-1}
        sums = 0

        for i in range(len(nums)):
            sums += nums[i]
            if k != 0:
                remainder = sums % k

            if remainder in rema_f:
                if i - rema_f[remainder] >= 2:
                    return True
            else:
                rema_f[remainder] = i
        
        return False
