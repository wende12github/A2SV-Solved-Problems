class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        pre_dict = dict()
        pre_dict[0] = 1
        
        for i in range(len(nums)):
            prefix_sum += nums[i]
            count += pre_dict.get(prefix_sum-k,0)
            pre_dict[prefix_sum] = pre_dict.get(prefix_sum,0) + 1
        
        return(count)
