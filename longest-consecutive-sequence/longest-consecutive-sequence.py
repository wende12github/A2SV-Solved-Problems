class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return n

        result = 1
        nums.sort()
        value = nums[0]
        count = 1

        for i in range(1, n):
            temp = value + 1
            if nums[i] == value:
                continue

            if nums[i] == temp:
                count += 1
                value += 1
                result = max(result, count)
            else:
                value = nums[i]
                count = 1

        return max(result, count)
