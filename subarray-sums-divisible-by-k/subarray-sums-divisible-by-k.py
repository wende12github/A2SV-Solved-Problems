class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        result = 0
        prefix_counter = defaultdict(int)
        prefix_counter[0] = 1

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            result += prefix_counter[remainder]
            prefix_counter[remainder] += 1

        return result
