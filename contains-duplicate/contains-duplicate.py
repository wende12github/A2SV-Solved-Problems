class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = set()

        for num in nums:
            if num in result:
                return True

            else:
                result.add(num)
                

        return False
