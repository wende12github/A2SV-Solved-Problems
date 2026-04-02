class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] == target:
                return mid
            else:
                low = mid + 1

        if nums[mid] < target:
            result = 1 + mid
        else:
            result = low

        return result
