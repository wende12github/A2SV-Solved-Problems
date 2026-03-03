class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        majority = nums[0]
        frequency = 1
        prefix_count = 0
        max_frequency = 0

        for num in nums:
            if num == majority:
                frequency += 1
            else: 
                frequency -= 1

            if frequency == 0:
                majority = num
                frequency = 1

        for num in nums
            if num == majority:
                max_frequency += 1

        for i in range(n):
            if nums[i] == majority:
                prefix_count += 1
                max_frequency -= 1
            if (prefix_count * 2 > (i + 1)) and (max_frequency * 2 > (n - i - 1)):
                return i

        return -1
