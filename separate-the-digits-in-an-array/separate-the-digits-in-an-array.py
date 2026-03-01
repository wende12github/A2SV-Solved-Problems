class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            temp_res = []
            while num >= 1:
                temp = num % 10
                temp_res.append(temp)
                num = num // 10
                
            temp_res.reverse()
            result.extend(temp_res)

        return result
