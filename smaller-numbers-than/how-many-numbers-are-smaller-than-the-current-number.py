class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp_nums = sorted(nums)
        mapping_freq = {}
        result = []
        n = len(nums)

        for i in range(n):
            if temp_nums[i] not in mapping_freq:
                mapping_freq[temp_nums[i]] = i

        for i in range(n):
            result.append(mapping_freq[nums[i]])

        return result
