import bisect
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = []
        sor_num = []

        for n in reversed(nums):
            m = bisect.bisect_left(sor_num, n)
            result.append(m)

            bisect.insort(sor_num, n)

        return result[::-1]