class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        length = len(nums)
        stack = []

        if length < 3:
            return False

        max_valid = float('-inf')

        for i in range(length-1, -1, -1):
            num_current = nums[i]
            
            if num_current < max_valid:
                return True

            while stack and stack[-1] < num_current:
                max_valid = stack.pop()


            stack.append(num_current)

        return False

        