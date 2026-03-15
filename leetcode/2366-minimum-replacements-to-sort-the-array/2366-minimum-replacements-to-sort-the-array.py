class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operation = 0

        n = len(nums)
        
        last_num = nums[n-1]
        for i in range(n-2, -1, -1):
            if last_num < nums[i]:
                temp_num = nums[i] // last_num

                if nums[i] % last_num:
                    temp_num += 1

                operation += temp_num - 1
                last_num = nums[i] // temp_num
            else:
                last_num = nums[i]

        return operation